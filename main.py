import flet as ft

from src.navigation.screen_selection import ScreenSelection


class Main:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.theme = ft.Theme(
            page_transitions=ft.PageTransitionsTheme(windows=ft.PageTransitionTheme.FADE_UPWARDS))
        self.page.window.width = 1280
        self.page.window.height = 720
        self.page.window.resizable = False
        self.page.go("/")

    def route_change(self, rt):
        if rt.route in ScreenSelection.Screens:
            new_view = ScreenSelection.Screens[rt.route]
            self.page.views.append(new_view(self.page))
        self.page.update()

    def view_pop(self, event):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


ft.app(Main)
