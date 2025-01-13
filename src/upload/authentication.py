import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

class Authentication:
    YOUTUBE_UPLOAD_SCOPE = ["https://www.googleapis.com/auth/youtube.upload"]
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    USER_CREDENTIALS = {
        "web": {
            "client_id": None,
            "client_secret": None,
            "redirect_uris": ["https://localhost:8080"],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://accounts.google.com/o/oauth2/token"
        }
    }

    @staticmethod
    def get_authenticated_service(page):
        client_id = page.client_storage.get("client_id")
        client_secret = page.client_storage.get("client_secret")
        client_creds = page.client_storage.get("client_creds")

        Authentication.USER_CREDENTIALS["web"]["client_id"] = client_id
        Authentication.USER_CREDENTIALS["web"]["client_secret"] = client_secret

        creds = None
        if client_creds is not None:
            client_creds = json.loads(client_creds)
            try:
                creds = Credentials.from_authorized_user_info(client_creds, Authentication.YOUTUBE_UPLOAD_SCOPE)
            except ValueError:
                return False
            if creds.valid:
                return True



        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_config(Authentication.USER_CREDENTIALS, Authentication.YOUTUBE_UPLOAD_SCOPE)
                flow.run_local_server(port=8080)
                flow.authorization_url(access_type='offline')
                creds = flow.credentials

            if creds.valid:
                credentials_json = creds.to_json()
                page.client_storage.set("client_creds", credentials_json)
                print(credentials_json)
                if creds.refresh_token is None:
                    return False
                return True

        return False

