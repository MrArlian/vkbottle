from ..base import VkObject

from vkbottle.enum.vk_object import CallbackGroupJoinType


class GroupJoin(VkObject):
    join_type: CallbackGroupJoinType
    user_id: int
