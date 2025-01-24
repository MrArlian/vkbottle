from enum import IntEnum


class ErrorCode(IntEnum):
    """ Error code """

    notifications_disabled = 1
    flood_control_per_hour = 2
    flood_control_per_day = 3
    app_is_not_installed = 4
