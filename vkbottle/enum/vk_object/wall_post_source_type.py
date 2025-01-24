from enum import StrEnum


class WallPostSourceType(StrEnum):
    """ Type of post source """

    VK = "vk"
    WIDGET = "widget"
    API = "api"
    RSS = "rss"
    SMS = "sms"
    MVK = "mvk"
