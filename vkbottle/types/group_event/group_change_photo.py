from ..base import VkObject

from ..object.photos import Photo


class GroupChangePhoto(VkObject):
    photo: Photo
    user_id: int
