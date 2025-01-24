from enum import StrEnum


class FeedItemType(StrEnum):
    """ Type of Feed Item """

    PROMO_STORIES = "promo_stories"
    STORIES = "stories"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    COMMUNITY_GROUPED_STORIES = "community_grouped_stories"
    APP_GROUPED_STORIES = "app_grouped_stories"
    BIRTHDAY = "birthday"
    DISCOVER = "discover"
    ADVICES = "advices"
