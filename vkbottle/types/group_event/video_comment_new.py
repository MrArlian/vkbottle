from ..object.wall import WallComment


class VideoCommentNew(WallComment):
    video_id: int
    video_owner_id: int
