from googleapiclient.http import MediaFileUpload
import flet as ft
import asyncio


class VideoUploader:

    def __init__(self, page: ft.Page):
        self.page = page

    def initialize_upload(self, youtube, options):
        body = dict(
            snippet = dict(
                title=options.title,
                description=options.description,
            ),
            status=dict(
                privacyStatus=options.privacyStatus
            )
        )
        insert_request = youtube.videos().insert(
            part=",".join(body.keys()),
            body=body,
            media_body=MediaFileUpload(options.file, chunksize=4*1024*1024, resumable=True)
        )
        self.resumable_upload(insert_request)

    def resumable_upload(self, insert_request):
        return

    async def test(self):
        await asyncio.sleep(3)
        return 100
