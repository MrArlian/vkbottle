from ..base import VkObject

from vkbottle.enum.vk_object import CallbackGroupOfficerRole


class GroupOfficersEdit(VkObject):
    admin_id: int
    level_new: CallbackGroupOfficerRole
    level_old: CallbackGroupOfficerRole
    user_id: int
