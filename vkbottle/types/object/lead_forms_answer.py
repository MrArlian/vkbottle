from __future__ import annotations

from typing import TYPE_CHECKING, Union, List

from ..base import VkObject

if TYPE_CHECKING:
    from .lead_forms_answer_item import LeadFormsAnswerItem


class LeadFormsAnswer(VkObject):
    """VK Object LeadFormsAnswer"""

    answer: Union[LeadFormsAnswerItem, List[LeadFormsAnswerItem]]
    key: str
