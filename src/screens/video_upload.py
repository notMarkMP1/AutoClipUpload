import flet as ft
from src.upload.upload import VideoUploader
import asyncio

class VideoUpload(ft.View):

    async def begin_upload(self):
        video_uploader = VideoUploader()
        # r = await video_uploader.test(self.page, self.upload_size_status, self.upload_progress_bar)
        self.page.update()
        r = await video_uploader.initialize_upload(self.creds, self.options, self.video_size, self.upload_size_status, self.upload_progress_bar, self.page)
        if 'id' in r:
            self.page.launch_url(f"https://youtube.com/watch?v={r['id']}")
        self.page.update()

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        video = self.page.client_storage.get("video")[0]
        self.video_size = video['size']
        media = [
            ft.VideoMedia(
                video['path']
            )
        ]

        video_player = ft.Video(
            playlist=media,
            expand=True
        )

        appbar = ft.AppBar(
            title=ft.Text("Video Upload"),
            center_title=True,
        )

        self.upload_size_status = ft.Text(
            value="Uploading: 0MB / " + str(round(self.video_size/1000000, 2)) + "MB" # converts bytes to megabytes
        )

        self.upload_progress_bar = ft.ProgressBar(
            height=10,
            value=0
        )

        self.controls = [
            appbar,
            video_player,
            ft.Column(
                controls=[
                    self.upload_size_status,
                    self.upload_progress_bar,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        ]
        self.page.update()
        self.creds = self.page.client_storage.get("client_creds")
        self.video_title = self.page.client_storage.get("video title")
        self.video_visibility = self.page.client_storage.get("video visibility")
        self.video_description = self.page.client_storage.get("video description")
        self.options = {"title": self.video_title,
                        "description": self.video_description,
                        "privacyStatus": self.video_visibility,
                        "file": video['path']}

        page.run_task(self.begin_upload)

