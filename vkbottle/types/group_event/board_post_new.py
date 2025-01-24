from typing import Optional

from ..object.board.topic_comment import TopicComment


class BoardPostNew(TopicComment):
    topic_id: Optional[int] = None
    topic_owner_id: Optional[int] = None
