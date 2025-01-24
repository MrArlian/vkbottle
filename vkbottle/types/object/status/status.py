from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..audio_audio import AudioAudio


class Status(VkObject):
    """VK Object StatusStatus

    audio -
    text - Status text
    """

    audio: Optional[AudioAudio] = None
    text: str
