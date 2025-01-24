from src.navigation.route_names import RouteNames

from src.screens.home import Home
from src.screens.configuration import Configuration
from src.screens.video_options import VideoOptions
from src.screens.video_upload import VideoUpload

class ScreenSelection:
    Screens = {
        RouteNames.HOME_ROUTE: Home,
        RouteNames.CONFIGURATION_ROUTE: Configuration,
        RouteNames.VIDEO_ROUTE: VideoOptions,
        RouteNames.UPLOAD_ROUTE: VideoUpload
    }
