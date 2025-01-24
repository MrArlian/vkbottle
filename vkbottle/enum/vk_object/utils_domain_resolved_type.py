from enum import StrEnum


class UtilsDomainResolvedType(StrEnum):
    """ Object type """

    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    PAGE = "page"
    VK_APP = "vk_app"
    COMMUNITY_APPLICATION = "community_application"
