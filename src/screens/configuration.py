import flet as ft
from src.upload.authentication import Authentication


class Configuration(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        def show_help(e):
            self.page.open(help_dialog)

        def save_action(e, action):
            if action == "id":
                self.page.client_storage.set("client_id", client_id_textbox.value)
            elif action == "secret":
                self.page.client_storage.set("client_secret", client_secret_textbox.value)

        def get_auth(e):
            Authentication.get_authenticated_service(self.page)

        def delete_credentials(e):
            self.page.client_storage.remove("client_id")
            self.page.client_storage.remove("client_secret")
            self.page.client_storage.remove("client_credentials")
            client_id_textbox.value = ""
            client_secret_textbox.value = ""
            self.page.update()

        self.padding = 20

        help_dialog = ft.AlertDialog(
            title=ft.Text("Help"),
            content=ft.Text(
                "Client ID is a unique identifier provided by the service you are connecting to. Make sure to use the correct ID."),
            actions=[ft.TextButton("Close", on_click=lambda e: self.page.close(help_dialog))],
        )

        self.dialog = help_dialog

        appbar = ft.AppBar(
            title=ft.Text("Configuration"),
            center_title=True
        )
        client_id_textbox = ft.TextField(
            label="Client ID",
            width=400,
            border_color=ft.Colors.GREY,
            focused_border_color=ft.Colors.WHITE,
            value=self.page.client_storage.get("client_id"))

        client_secret_textbox = ft.TextField(
            label="Client Secret",
            width=400,
            border_color=ft.Colors.GREY,
            focused_border_color=ft.Colors.WHITE,
            value=self.page.client_storage.get("client_secret")
        )

        client_id_help = ft.IconButton(icon=ft.Icons.HELP_OUTLINE, on_click=show_help)

        save_button_id = ft.ElevatedButton(
            text="Save",
            on_click= lambda e: save_action(e, "id")
        )

        save_button_secret = ft.ElevatedButton(
            text="Save",
            on_click= lambda e: save_action(e, "secret")
        )

        oauth_signin_button = ft.ElevatedButton(
            text="OAuth Sign In",
            bgcolor=ft.Colors.GREEN,
            color=ft.Colors.WHITE,
            icon=ft.Icons.KEY,
            on_click=get_auth
        )

        delete_credentials_button = ft.ElevatedButton(
            text="Delete Credentials",
            bgcolor=ft.Colors.RED,
            color=ft.Colors.WHITE,
            icon=ft.Icons.DELETE_FOREVER_SHARP,
            on_click=delete_credentials
        )



        self.controls = [
            appbar,
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row([client_id_help, client_id_textbox, save_button_id], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([client_id_help, client_secret_textbox, save_button_secret], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([oauth_signin_button, delete_credentials_button], alignment=ft.MainAxisAlignment.CENTER)
                    ],
                    spacing=20,
                ),
                padding=ft.padding.all(20),
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.SURFACE,
                border_radius=10,
                shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.SHADOW),
            )
        ]
