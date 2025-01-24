from enum import IntEnum


class WallWallpostFullTopicId(IntEnum):
    """ Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method """

    empty_topic = 0
    art = 1
    it = 7
    games = 12
    music = 16
    photo = 19
    science_and_tech = 21
    sport = 23
    travel = 25
    tv_and_cinema = 26
    humor = 32
    fashion = 43
