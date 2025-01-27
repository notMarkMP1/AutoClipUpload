import flet as ft
from src.upload.upload import VideoUploader
import time

class VideoUpload(ft.View):

    def begin_upload(self):
        uploader = VideoUploader(self.page)
        uploader.test()


    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        video = self.page.client_storage.get("video")[0]

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

        upload_size_status = ft.Text(
            value="Uploading..."
        )

        upload_progress_bar = ft.ProgressBar(
            value=0.5,
            height=10
        )

        self.controls = [
            appbar,
            video_player,
            ft.Column(
                controls=[
                    upload_size_status,
                    upload_progress_bar,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        ]
        self.page.update()
