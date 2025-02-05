import flet as ft
from src.navigation.route_names import RouteNames
from src.upload.authentication import Authentication

class Home(ft.View):

    def on_configuration_click(self, e):
        # self.page.overlay.append(ft.SnackBar(content=ft.Text("Configuration clicked"), open=True, duration=1000))
        self.page.go(RouteNames.CONFIGURATION_ROUTE)
        self.page.update()

    def on_select_files(self, e):
        self.page.overlay.append(self.pick_files_dialog)
        self.page.update()

        self.pick_files_dialog.pick_files(allowed_extensions=["mp4", "mkv", "mov", "avi"])

    def file_selection_action(self, e: ft.FilePickerResultEvent):
        auth = Authentication()
        request = auth.get_authenticated_service_existing(self.page)

        if request and e.files is not None:
            self.page.client_storage.set("video", e.files)
            self.page.go(RouteNames.VIDEO_ROUTE)
            self.page.update()
        else:
            self.page.open(self.dlg)



    def __init__(self, page: ft.Page):
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

        self.pick_files_dialog = ft.FilePicker(on_result=self.file_selection_action)

        select_files_button = ft.ElevatedButton(
            text="Select Files",
            icon=ft.Icons.UPLOAD_FILE,
            on_click=self.on_select_files,
            bgcolor="green",
            color="white",
        )

        self.dlg = ft.AlertDialog(
            title=ft.Text("Please validate your credentials before uploading videos."),
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
