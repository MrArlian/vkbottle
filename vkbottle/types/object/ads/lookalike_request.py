from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import (
    LookalikeRequestStatus,
    LookalikeRequestSourceType
)

from ...base import VkObject

if TYPE_CHECKING:
    from .lookalike_request_save_audience_level import LookalikeRequestSaveAudienceLevel


class LookalikeRequest(VkObject):
    """VK Object AdsLookalikeRequest

    audience_count - Lookalike request seed audience size
    create_time - Lookalike request create time, as Unixtime
    id - Lookalike request ID
    save_audience_levels -
    scheduled_delete_time - Time by which lookalike request would be deleted, as Unixtime
    source_name - Lookalike request seed name (retargeting group name)
    source_retargeting_group_id - Retargeting group id, which was used as lookalike seed
    source_type - Lookalike request source type
    status - Lookalike request status
    update_time - Lookalike request update time, as Unixtime
    """

    audience_count: Optional[int] = None
    create_time: int
    id: int
    save_audience_levels: Optional[List[LookalikeRequestSaveAudienceLevel]] = None
    scheduled_delete_time: Optional[int] = None
    source_name: Optional[str] = None
    source_retargeting_group_id: Optional[int] = None
    source_type: LookalikeRequestSourceType
    status: LookalikeRequestStatus
    update_time: int
