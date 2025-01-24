from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .base_request_param import BaseRequestParam


class BaseError(VkObject):
    """VK Object BaseError

    error_code - Error code
    error_msg - Error message
    error_subcode - Error subcode
    error_text - Localized error message
    request_params -
    """

    error_code: int
    error_msg: Optional[str] = None
    error_subcode: Optional[int] = None
    error_text: Optional[str] = None
    request_params: Optional[List[BaseRequestParam]] = None
