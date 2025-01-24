from typing import Optional

from vkbottle.enum.vk_object import CallbackLikeAddRemoveObjectType

from ..base import VkObject


class LikeAdd(VkObject):
    liker_id: int
    object_id: int
    object_owner_id: int
    object_type: Optional[CallbackLikeAddRemoveObjectType] = None
    post_id: int
    thread_reply_id: Optional[int] = None
