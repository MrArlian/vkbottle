from ..object.wall import WallComment


class PhotoCommentNew(WallComment):
    photo_id: int
    photo_owner_id: int
