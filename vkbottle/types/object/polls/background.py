from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import PollsBackgroundType

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_image import BaseImage
    from ..base_gradient_point import BaseGradientPoint


class Background(VkObject):
    """VK Object PollsBackground

    angle - Gradient angle with 0 on positive X axis
    color - Hex color code without #
    height - Original height of pattern tile
    id -
    images - Pattern tiles
    name -
    points - Gradient points
    type -
    width - Original with of pattern tile
    """

    angle: Optional[int] = None
    color: Optional[str] = None
    height: Optional[int] = None
    id: Optional[int] = None
    images: Optional[List[BaseImage]] = None
    name: Optional[str] = None
    points: Optional[List[BaseGradientPoint]] = None
    type: Optional[PollsBackgroundType] = None
    width: Optional[int] = None
