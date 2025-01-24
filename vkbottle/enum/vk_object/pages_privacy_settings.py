from enum import IntEnum


class PagesPrivacySettings(IntEnum):
    """ PagesPrivacySettings enum """

    community_managers_only = 0
    community_members_only = 1
    everyone = 2
