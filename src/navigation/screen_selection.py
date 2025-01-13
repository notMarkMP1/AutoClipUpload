from src.navigation.route_names import RouteNames

from src.screens.home import Home
from src.screens.configuration import Configuration


class ScreenSelection:
    Screens = {
        RouteNames.HOME_ROUTE: Home,
        RouteNames.CONFIGURATION_ROUTE: Configuration,
    }
