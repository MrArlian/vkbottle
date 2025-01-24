from enum import StrEnum


class StoriesStoryType(StrEnum):
    """ Story type. """

    PHOTO = "photo"
    VIDEO = "video"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    BIRTHDAY_INVITE = "birthday_invite"
