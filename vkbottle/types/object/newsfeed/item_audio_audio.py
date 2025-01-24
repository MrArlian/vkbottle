from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..audio_audio import AudioAudio


class ItemAudioAudio(VkObject):
    """VK Object NewsfeedItemAudioAudio

    count - Audios number
    items -
    """

    count: Optional[int] = None
    items: Optional[List[AudioAudio]] = None
