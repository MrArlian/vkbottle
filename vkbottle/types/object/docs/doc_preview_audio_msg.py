from __future__ import annotations

from typing import List

from ...base import VkObject


class DocPreviewAudioMsg(VkObject):
    """VK Object DocsDocPreviewAudioMsg

    duration - Audio message duration in seconds
    link_mp3 - MP3 file URL
    link_ogg - OGG file URL
    waveform -
    """

    duration: int
    link_mp3: str
    link_ogg: str
    waveform: List[int]
