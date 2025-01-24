from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import LeadFormsQuestionItemType

from ..base import VkObject

if TYPE_CHECKING:
    from .lead_forms_question_item_option import LeadFormsQuestionItemOption


class LeadFormsQuestionItem(VkObject):
    """VK Object LeadFormsQuestionItem

    key -
    label -
    options - Опции выбора для типов radio, checkbox, select
    type -
    """

    key: str
    label: Optional[str] = None
    options: Optional[List[LeadFormsQuestionItemOption]] = None
    type: LeadFormsQuestionItemType
