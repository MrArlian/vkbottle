from enum import StrEnum


class RelativeType(StrEnum):
    """ Relative type """

    PARENT = "parent"
    CHILD = "child"
    GRANDPARENT = "grandparent"
    GRANDCHILD = "grandchild"
    SIBLING = "sibling"
