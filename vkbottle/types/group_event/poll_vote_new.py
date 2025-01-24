from ..base import VkObject


class PollVoteNew(VkObject):
    option_id: int
    owner_id: int
    poll_id: int
    user_id: int
