from __future__ import annotations

from typing import Optional

from ..base import VkObject


class OauthError(VkObject):
    """VK Object OauthError

    error - Error type
    error_description - Error description
    redirect_uri - URI for validation
    """

    error: str
    error_description: str
    redirect_uri: Optional[str] = None
