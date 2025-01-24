import flet as ft
from src.navigation.route_names import RouteNames

class VideoOptions(ft.View):

    def upload_click(self, e):
        self.video_player.stop()
        self.page.go(RouteNames.UPLOAD_ROUTE)

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        video = self.page.client_storage.get("video")[0]

        media = [
            ft.VideoMedia(
                video['path']
            )
        ]

        self.video_player = ft.Video(
            playlist=media,
            autoplay=True,
            aspect_ratio=16/9,
            expand=True
        )

        appbar = ft.AppBar(
            title=ft.Text("Video Options"),
            center_title=True
        )

        video_title = ft.TextField(label="Video Title", width=400, value=video['name'])
        video_description = ft.TextField(label="Video Description", width=400, multiline=True, max_lines=10)

        video_visibility = ft.Dropdown(
            label="Video Visibility",
            options=[
                ft.dropdown.Option("Public"),
                ft.dropdown.Option("Private"),
                ft.dropdown.Option("Unlisted")
            ],
            width=400
        )

        modify_button = ft.ElevatedButton(
            text="Modify Video",
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
            icon=ft.Icons.MOVIE_EDIT
        )
        upload_button = ft.ElevatedButton(
            text="Upload Video",
            bgcolor=ft.Colors.GREEN,
            color=ft.Colors.WHITE,
            icon=ft.Icons.FILE_UPLOAD,
            on_click=self.upload_click
        )

        video_size_text = ft.Text(
            value="Video size: " + str(round(video['size']/1000000, 2)) + "MB"
        )

        self.controls = [
            appbar,
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            self.video_player,
                            ft.Column(
                                controls=[
                                    video_title,
                                    video_description,
                                    video_visibility,
                                    ft.Row(
                                        controls=[modify_button, upload_button],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=20,
                                        width=400
                                    ),
                                    video_size_text
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=20
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        ]
