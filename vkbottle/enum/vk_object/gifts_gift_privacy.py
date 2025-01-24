from enum import IntEnum


class GiftsGiftPrivacy(IntEnum):
    """ Gift privacy """

    name_and_message_for_all = 0
    name_for_all = 1
    name_and_message_for_recipient_only = 2
