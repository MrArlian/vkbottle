from enum import StrEnum


class NewsfeedIgnoreItemType(StrEnum):
    """ NewsfeedIgnoreItemType enum """

    WALL = "wall"
    TAG = "tag"
    PROFILEPHOTO = "profilephoto"
    VIDEO = "video"
    PHOTO = "photo"
    AUDIO = "audio"
