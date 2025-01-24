import flet as ft

class VideoOptions(ft.View):
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
            width=640,
            height=360
        )

        appbar = ft.AppBar(
            title=ft.Text("Video Options"),
            center_title=True
        )

        video_title = ft.TextField(label="Video Title", width=400)
        video_description = ft.TextField(label="Video Description", width=400, multiline=True)

        video_visibility = ft.Dropdown(
            label="Video Visibility",
            options=[
                ft.dropdown.Option("Public"),
                ft.dropdown.Option("Private"),
                ft.dropdown.Option("Unlisted")
            ],
            width=400
        )

        modify_button = ft.ElevatedButton("Modify Video")
        upload_button = ft.ElevatedButton("Upload Video")

        self.controls = [
            appbar,
            ft.Row(
                controls=[
                    video_player,
                    ft.Column(
                        controls=[
                            video_title,
                            video_description,
                            video_visibility,
                            ft.Row(
                                controls=[modify_button, upload_button],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=20
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            )
        ]