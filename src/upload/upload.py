from googleapiclient.http import MediaFileUpload
import asyncio
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import http.client as httplib
import httplib2
import json


class VideoUploader:
    RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, httplib.NotConnected,
                            httplib.IncompleteRead, httplib.ImproperConnectionState,
                            httplib.CannotSendRequest, httplib.CannotSendHeader,
                            httplib.ResponseNotReady, httplib.BadStatusLine)
    RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
    YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    async def initialize_upload(self, creds, options, size, size_status, progress_bar, page):
        creds = json.loads(creds)
        try:
            creds = Credentials.from_authorized_user_info(creds, self.YOUTUBE_UPLOAD_SCOPE)
        except Exception as error:
            print(error)
            return
        youtube = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION, credentials=creds)
        body = dict(
            snippet=dict(
                title=options['title'],
                description=options['description'],
            ),
            status=dict(
                privacyStatus=options['privacyStatus']
            )
        )
        insert_request = youtube.videos().insert(
            part=",".join(body.keys()),
            body=body,
            media_body=MediaFileUpload(options['file'], chunksize=4 * 1024 * 1024, resumable=True)
        )
        await asyncio.sleep(1)
        r = await self.resumable_upload(insert_request, size, size_status, progress_bar, page)
        return r

    async def resumable_upload(self, insert_request, size, size_status, progress_bar, page):
        response = None
        error = None
        retry = 0
        print("Starting Upload.")
        while response is None:
            try:
                status, response = insert_request.next_chunk()
                if status is not None:
                    await asyncio.sleep(0)
                    progress_bytes = status.progress() * size
                    size_status.value = str("Uploading: " + str(round(progress_bytes / 1000000, 2)) + "MB / " + str(round(size / 1000000, 2)) + "MB")
                    progress_bar.value = status.progress()
                    page.update()
                    print("Uploading file:", str(status.progress() * 100) + "%")
                if response is not None:
                    if 'id' in response:
                        size_status.value = str("Video id '%s' was successfully uploaded." % response['id'])
                        page.update()
                        return response
                    else:
                        return response
                        # exit("The upload failed with an unexpected response: %s" % response)
            except HttpError as e:
                if e.resp.status in self.RETRIABLE_STATUS_CODES:
                    error = "A retriable HTTP error %d occurred:\n%s" % (e.resp.status,
                                                                         e.content)
                else:
                    raise
            except self.RETRIABLE_EXCEPTIONS as e:
                error = "A retriable error occurred: %s" % e
        if error is not None:
            print(error)
            retry += 1
            if retry > 5:
                exit("No longer attempting to retry.")

            sleep_seconds = 3
            print("Sleeping %f seconds and then retrying..." % sleep_seconds)
            await asyncio.sleep(sleep_seconds)

    async def test(self, page, upload_size_status, progress_bar):
        await asyncio.sleep(3)
        upload_size_status.value = "3"
        progress_bar.value = 0.5
        page.update()
        await asyncio.sleep(2)
        print("hi")
        return 100  # Returning the progress value
