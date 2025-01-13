import flet as ft
from datetime import datetime
import json
from src.upload.authentication import Authentication


class Configuration(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        def highlight_link(e):
            e.control.style.color = ft.Colors.PURPLE
            e.control.update()

        def unhighlight_link(e):
            e.control.style.color = ft.Colors.BLUE
            e.control.update()

        def show_help(e):
            self.page.open(help_dialog)

        def save_action(e, action):
            action_text.spans = None
            if action == "id":
                self.page.client_storage.set("client_id", client_id_textbox.value.strip())
                action_text.color = ft.Colors.WHITE
                action_text.value = "Client ID saved."
            elif action == "secret":
                self.page.client_storage.set("client_secret", client_secret_textbox.value.strip())
                action_text.color = ft.Colors.WHITE
                action_text.value = "Client Secret saved."
            self.page.update()

        def get_auth(e):
            request = Authentication.get_authenticated_service(self.page)
            if request:
                client_creds = json.loads(self.page.client_storage.get("client_creds"))
                timestamp = datetime.strptime(client_creds['expiry'], "%Y-%m-%dT%H:%M:%S.%fZ")
                readable_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                action_text.color = ft.Colors.GREEN
                action_text.spans = None
                action_text.value = f"Credentials are valid. Expires: {readable_timestamp}"
            else:
                action_text.color = ft.Colors.RED
                action_text.spans = None
                action_text.value = "Credentials could not be validated. Please clear credentials and try again."
            self.page.update()

        def delete_credentials(e):
            self.page.client_storage.remove("client_id")
            self.page.client_storage.remove("client_secret")
            self.page.client_storage.remove("client_creds")
            client_id_textbox.value = ""
            client_secret_textbox.value = ""
            action_text.color = ft.Colors.RED_500
            action_text.value = None
            action_text.spans = [ft.TextSpan("Credentials have been removed. Also visit "),
                                 ft.TextSpan("this link",
                                             ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, color=ft.Colors.BLUE),
                                             url="https://myaccount.google.com/connections?filters=3,4&hl=en",
                                             on_enter=highlight_link,
                                             on_exit=unhighlight_link), ft.TextSpan(" and delete 'AutoClipUpload'.")]
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
            on_click=lambda e: save_action(e, "id")
        )

        save_button_secret = ft.ElevatedButton(
            text="Save",
            on_click=lambda e: save_action(e, "secret")
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

        action_text = ft.Text()

        if self.page.client_storage.get("client_creds") is not None:
            get_auth(None)

        self.controls = [
            appbar,
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row([client_id_help, client_id_textbox, save_button_id], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([client_id_help, client_secret_textbox, save_button_secret], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([oauth_signin_button, delete_credentials_button], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([action_text], alignment=ft.MainAxisAlignment.CENTER)
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
