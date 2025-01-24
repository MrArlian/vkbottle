from enum import StrEnum


class NewsfeedCommentsFilters(StrEnum):
    """ NewsfeedCommentsFilters enum """

    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"
