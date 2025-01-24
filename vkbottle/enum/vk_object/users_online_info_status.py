from enum import StrEnum


class UsersOnlineInfoStatus(StrEnum):
    """ In case user online is not visible, it indicates approximate timeframe of user online """

    RECENTLY = "recently"
    LAST_WEEK = "last_week"
    LAST_MONTH = "last_month"
    LONG_AGO = "long_ago"
    NOT_SHOW = "not_show"
