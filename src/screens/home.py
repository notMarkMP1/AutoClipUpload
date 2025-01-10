import flet as ft
from src.navigation.route_names import RouteNames


class Home(ft.View):

    def on_configuration_click(self, e):
        # self.page.overlay.append(ft.SnackBar(content=ft.Text("Configuration clicked"), open=True, duration=1000))
        self.page.go(RouteNames.CONFIGURATION_ROUTE)
        self.page.update()

    def on_select_files_click(self, e):
        self.page.overlay.append(ft.SnackBar(content=ft.Text("Select files clicked"), open=True, duration=1000))
        self.page.update()
    def __init__(self):
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.padding = 20

        title = ft.Text(
            "Welcome to AutoClipUpload",
            size=30,
            weight=ft.FontWeight.BOLD,
            color="blue",
            text_align=ft.TextAlign.CENTER
        )

        description = ft.Text(
            "Your ultimate tool for automating clip uploads.",
            size=18,
            text_align=ft.TextAlign.CENTER
        )

        configuration_button = ft.ElevatedButton(
            text="Configuration",
            icon=ft.Icons.SETTINGS,
            on_click=self.on_configuration_click,
            bgcolor="lightblue",
            color="white",
        )

        select_files_button = ft.ElevatedButton(
            text="Select Files",
            icon=ft.Icons.UPLOAD_FILE,
            on_click=self.on_select_files_click,
            bgcolor="green",
            color="white",
        )
        self.controls = [
            ft.Column(
                controls=[
                    title,
                    description,
                    ft.Row(
                        controls=[
                            select_files_button,
                            configuration_button
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
