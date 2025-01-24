import flet as ft
class VideoUpload(ft.View):
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
            autoplay=True,
            aspect_ratio=16/9,
            expand=True
        )

        appbar = ft.AppBar(
            title=ft.Text("Video Upload"),
            center_title=True,
        )

        self.controls = [
            appbar,
            ft.Column(
                controls=[
                    video_player
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]