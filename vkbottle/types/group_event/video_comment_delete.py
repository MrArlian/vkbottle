from ..base import VkObject


class VideoCommentDelete(VkObject):
    id: int
    deleter_id: int
    owner_id: int
    user_id: int
    video_id: int
