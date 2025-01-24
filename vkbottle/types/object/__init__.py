from typing import List, Optional, Union

from .app_widgets_photos import AppWidgetsPhotos
from .pretty_cards_pretty_card import PrettyCardsPrettyCard
from .base_link_application_store import BaseLinkApplicationStore
from .adsweb_get_fraud_history_response_entries_entry import AdswebGetFraudHistoryResponseEntriesEntry
from .podcast_cover import PodcastCover
from .link_target_object import LinkTargetObject
from .base_object_with_name import BaseObjectWithName
from .base_error import BaseError
from .lead_forms_question_item import LeadFormsQuestionItem
from .base_sticker_old import BaseStickerOld
from .base_likes import BaseLikes
from .podcast_external_data import PodcastExternalData
from .stickers_image_set import StickersImageSet
from .base_link_button_action import BaseLinkButtonAction
from .comment_thread import CommentThread
from .base_object import BaseObject
from .lead_forms_lead import LeadFormsLead
from .events_event_attach import EventsEventAttach
from .app_widgets_photo import AppWidgetsPhoto
from .base_city import BaseCity
from .base_link_application import BaseLinkApplication
from .base_link_rating import BaseLinkRating
from .lead_forms_answer_item import LeadFormsAnswerItem
from .base_comments_info import BaseCommentsInfo
from .client_info_for_bots import ClientInfoForBots
from .lead_forms_form import LeadFormsForm
from .lead_forms_answer import LeadFormsAnswer
from .base_sticker_animation import BaseStickerAnimation
from .base_gradient_point import BaseGradientPoint
from .base_user_id import BaseUserId
from .adsweb_get_sites_response_sites_site import AdswebGetSitesResponseSitesSite
from .base_place import BasePlace
from .base_crop_photo_rect import BaseCropPhotoRect
from .oauth_error import OauthError
from .base_request_param import BaseRequestParam
from .base_link_product import BaseLinkProduct
from .base_likes_info import BaseLikesInfo
from .base_crop_photo import BaseCropPhoto
from .base_geo_coordinates import BaseGeoCoordinates
from .base_reposts_info import BaseRepostsInfo
from .owner_state import OwnerState
from .audio_audio import AudioAudio
from .adsweb_get_statistics_response_items_item import AdswebGetStatisticsResponseItemsItem
from .base_image import BaseImage
from .base_sticker_new import BaseStickerNew
from .base_crop_photo_crop import BaseCropPhotoCrop
from .base_link_button import BaseLinkButton
from .base_link import BaseLink
from .adsweb_get_ad_categories_response_categories_category import AdswebGetAdCategoriesResponseCategoriesCategory
from .base_link_product_category import BaseLinkProductCategory
from .base_message_error import BaseMessageError
from .base_upload_server import BaseUploadServer
from .base_geo import BaseGeo
from .adsweb_get_ad_units_response_ad_units_ad_unit import AdswebGetAdUnitsResponseAdUnitsAdUnit
from .base_object_count import BaseObjectCount
from .lead_forms_question_item_option import LeadFormsQuestionItemOption
from .base_country import BaseCountry
from .calls.participants import Participants
from .calls.call import Call
from .docs.doc_types import DocTypes
from .docs.doc_preview_audio_msg import DocPreviewAudioMsg
from .docs.doc_preview_photo import DocPreviewPhoto
from .docs.doc_preview_photo_sizes import DocPreviewPhotoSizes
from .docs.doc_preview import DocPreview
from .docs.doc_preview_graffiti import DocPreviewGraffiti
from .docs.doc_preview_video import DocPreviewVideo
from .docs.doc import Doc
from .donut.donator_subscription_info import DonatorSubscriptionInfo
from .search.hint import Hint
from .market.market_category import MarketCategory
from .market.market_category_nested import MarketCategoryNested
from .market.order import Order
from .market.market_category_tree import MarketCategoryTree
from .market.currency import Currency
from .market.section import Section
from .market.market_album import MarketAlbum
from .market.market_item import MarketItem
from .market.price import Price
from .market.order_item import OrderItem
from .video.live_settings import LiveSettings
from .video.video_files import VideoFiles
from .video.live_info import LiveInfo
from .video.video_album import VideoAlbum
from .video.video_full import VideoFull
from .video.video import Video
from .video.save_result import SaveResult
from .video.video_image import VideoImage
from .orders.order import Order
from .orders.subscription import Subscription
from .orders.amount_item import AmountItem
from .orders.amount import Amount
from .status.status import Status
from .newsfeed.item_video_video import ItemVideoVideo
from .newsfeed.item_photo_tag_photo_tags import ItemPhotoTagPhotoTags
from .newsfeed.item_wallpost_feedback_answer import ItemWallpostFeedbackAnswer
from .newsfeed.item_audio_audio import ItemAudioAudio
from .newsfeed.item_digest_button import ItemDigestButton
from .newsfeed.item_base import ItemBase
from .newsfeed.item_digest_header import ItemDigestHeader
from .newsfeed.newsfeed_photo import NewsfeedPhoto
from .newsfeed.item_holiday_recommendations_block_header import ItemHolidayRecommendationsBlockHeader
from .newsfeed.item_wallpost_feedback import ItemWallpostFeedback
from .newsfeed.item_promo_button_action import ItemPromoButtonAction
from .newsfeed.item_promo_button_image import ItemPromoButtonImage
from .newsfeed.item_photo_photos import ItemPhotoPhotos
from .newsfeed.item_digest_footer import ItemDigestFooter
from .newsfeed.feed_list import FeedList
from .newsfeed.item_digest_full_item import ItemDigestFullItem
from .newsfeed.item_friend_friends import ItemFriendFriends
from .friends.mutual_friend import MutualFriend
from .friends.friends_list import FriendsList
from .friends.requests_xtr_message import RequestsXtrMessage
from .friends.requests_mutual import RequestsMutual
from .friends.requests import Requests
from .friends.friend_status import FriendStatus
from .pages.wikipage_history import WikipageHistory
from .pages.wikipage_full import WikipageFull
from .pages.wikipage import Wikipage
from .groups.counters_group import CountersGroup
from .groups.groups_array import GroupsArray
from .groups.callback_server import CallbackServer
from .groups.address import Address
from .groups.address_timetable_day import AddressTimetableDay
from .groups.cover import Cover
from .groups.subject_item import SubjectItem
from .groups.group_public_category_list import GroupPublicCategoryList
from .groups.long_poll_events import LongPollEvents
from .groups.long_poll_server import LongPollServer
from .groups.member_role import MemberRole
from .groups.links_item import LinksItem
from .groups.member_status_full import MemberStatusFull
from .groups.online_status import OnlineStatus
from .groups.live_covers import LiveCovers
from .groups.group_category_full import GroupCategoryFull
from .groups.group_tag import GroupTag
from .groups.long_poll_settings import LongPollSettings
from .groups.group_full import GroupFull
from .groups.addresses_info import AddressesInfo
from .groups.token_permission_setting import TokenPermissionSetting
from .groups.member_status import MemberStatus
from .groups.callback_settings import CallbackSettings
from .groups.group_category_type import GroupCategoryType
from .groups.group import Group
from .groups.group_attach import GroupAttach
from .groups.ban_info import BanInfo
from .groups.settings_twitter import SettingsTwitter
from .groups.group_ban_info import GroupBanInfo
from .groups.market_info import MarketInfo
from .groups.group_category import GroupCategory
from .groups.owner_xtr_ban_info import OwnerXtrBanInfo
from .groups.photo_size import PhotoSize
from .groups.contacts_item import ContactsItem
from .groups.address_timetable import AddressTimetable
from .stats.activity import Activity
from .stats.country import Country
from .stats.period import Period
from .stats.city import City
from .stats.reach import Reach
from .stats.sex_age import SexAge
from .stats.wallpost_stat import WallpostStat
from .stats.views import Views
from .notes.note_comment import NoteComment
from .notes.note import Note
from .gifts.gift import Gift
from .gifts.layout import Layout
from .notifications.send_message_error import SendMessageError
from .notifications.send_message_item import SendMessageItem
from .notifications.notification import Notification
from .notifications.reply import Reply
from .notifications.feedback import Feedback
from .notifications.notifications_comment import NotificationsComment
from .users.school import School
from .users.user_xtr_type import UserXtrType
from .users.university import University
from .users.military import Military
from .users.user_settings_xtr import UserSettingsXtr
from .users.last_seen import LastSeen
from .users.occupation import Occupation
from .users.user_min import UserMin
from .users.relative import Relative
from .users.exports import Exports
from .users.career import Career
from .users.personal import Personal
from .users.online_info import OnlineInfo
from .users.user import User
from .users.users_array import UsersArray
from .users.user_counters import UserCounters
from .users.user_connections import UserConnections
from .users.user_full import UserFull
from .database.school import School
from .database.university import University
from .database.station import Station
from .database.region import Region
from .database.faculty import Faculty
from .photos.photo import Photo
from .photos.tags_suggestion_item import TagsSuggestionItem
from .photos.photo_sizes import PhotoSizes
from .photos.tags_suggestion_item_button import TagsSuggestionItemButton
from .photos.photo_album_full import PhotoAlbumFull
from .photos.photo_full_xtr_real_offset import PhotoFullXtrRealOffset
from .photos.photo_upload import PhotoUpload
from .photos.photo_album import PhotoAlbum
from .photos.photo_tag import PhotoTag
from .photos.photo_xtr_tag_info import PhotoXtrTagInfo
from .photos.image import Image
from .photos.photo_xtr_real_offset import PhotoXtrRealOffset
from .store.stickers_keyword_sticker import StickersKeywordSticker
from .store.stickers_keyword import StickersKeyword
from .store.product import Product
from .widgets.widget_page import WidgetPage
from .widgets.widget_likes import WidgetLikes
from .widgets.comment_media import CommentMedia
from .widgets.comment_replies import CommentReplies
from .widgets.widget_comment import WidgetComment
from .widgets.comment_replies_item import CommentRepliesItem
from .board.topic import Topic
from .board.topic_comment import TopicComment
from .fave.tag import Tag
from .fave.page import Page
from .fave.bookmark import Bookmark
from .stories.feed_item import FeedItem
from .stories.promo_block import PromoBlock
from .stories.story_stats import StoryStats
from .stories.stat_line import StatLine
from .stories.story_stats_stat import StoryStatsStat
from .stories.clickable_area import ClickableArea
from .stories.clickable_sticker import ClickableSticker
from .stories.story_link import StoryLink
from .stories.replies import Replies
from .stories.clickable_stickers import ClickableStickers
from .stories.viewers_item import ViewersItem
from .stories.story import Story
from .secure.set_counter_item import SetCounterItem
from .secure.transaction import Transaction
from .secure.give_event_sticker_item import GiveEventStickerItem
from .secure.level import Level
from .secure.token_checked import TokenChecked
from .secure.sms_notification import SmsNotification
from .utils.link_stats import LinkStats
from .utils.link_checked import LinkChecked
from .utils.stats import Stats
from .utils.stats_extended import StatsExtended
from .utils.link_stats_extended import LinkStatsExtended
from .utils.domain_resolved import DomainResolved
from .utils.stats_sex_age import StatsSexAge
from .utils.stats_city import StatsCity
from .utils.short_link import ShortLink
from .utils.last_shortened_link import LastShortenedLink
from .utils.stats_country import StatsCountry
from .account.push_params import PushParams
from .account.offer import Offer
from .account.push_conversations import PushConversations
from .account.name_request import NameRequest
from .account.push_settings import PushSettings
from .account.account_counters import AccountCounters
from .account.info import Info
from .account.user_settings_interest import UserSettingsInterest
from .account.user_settings_interests import UserSettingsInterests
from .account.push_conversations_item import PushConversationsItem
from .messages.messages_array import MessagesArray
from .messages.message_action_photo import MessageActionPhoto
from .messages.keyboard_button_action_open_photo import KeyboardButtonActionOpenPhoto
from .messages.forward import Forward
from .messages.message_request_data import MessageRequestData
from .messages.longpoll_messages import LongpollMessages
from .messages.chat import Chat
from .messages.longpoll_params import LongpollParams
from .messages.pinned_message import PinnedMessage
from .messages.audio_message import AudioMessage
from .messages.conversation import Conversation
from .messages.foreign_message import ForeignMessage
from .messages.history_attachment import HistoryAttachment
from .messages.send_user_ids_response_item import SendUserIdsResponseItem
from .messages.chat_settings_photo import ChatSettingsPhoto
from .messages.graffiti import Graffiti
from .messages.push_settings import PushSettings
from .messages.keyboard_button_action_text import KeyboardButtonActionText
from .messages.chat_settings import ChatSettings
from .messages.message_action import MessageAction
from .messages.chat_restrictions import ChatRestrictions
from .messages.message_attachment import MessageAttachment
from .messages.chat_settings_acl import ChatSettingsAcl
from .messages.conversation_peer import ConversationPeer
from .messages.out_read_by import OutReadBy
from .messages.keyboard_button_action_open_link import KeyboardButtonActionOpenLink
from .messages.conversation_with_message import ConversationWithMessage
from .messages.keyboard_button_action_location import KeyboardButtonActionLocation
from .messages.chat_push_settings import ChatPushSettings
from .messages.chat_full import ChatFull
from .messages.get_conversation_members import GetConversationMembers
from .messages.message import Message
from .messages.keyboard import Keyboard
from .messages.chat_settings_permissions import ChatSettingsPermissions
from .messages.last_activity import LastActivity
from .messages.keyboard_button_action_callback import KeyboardButtonActionCallback
from .messages.keyboard_button_action_vkpay import KeyboardButtonActionVkpay
from .messages.conversation_sort_id import ConversationSortId
from .messages.chat_preview import ChatPreview
from .messages.keyboard_button import KeyboardButtonPropertyAction
from .messages.keyboard_button import KeyboardButton
from .messages.get_conversation_by_id import GetConversationById
from .messages.conversation_can_write import ConversationCanWrite
from .messages.history_message_attachment import HistoryMessageAttachment
from .messages.conversation_member import ConversationMember
from .messages.user_xtr_invited_by import UserXtrInvitedBy
from .messages.keyboard_button_action_open_app import KeyboardButtonActionOpenApp
from .apps.app import App
from .apps.scope import Scope
from .apps.catalog_list import CatalogList
from .apps.leaderboard import Leaderboard
from .apps.app_min import AppMin
from .ads.campaign import Campaign
from .ads.stats_views_times import StatsViewsTimes
from .ads.update_office_users_result import UpdateOfficeUsersResult
from .ads.ad_layout import AdLayout
from .ads.reject_reason import RejectReason
from .ads.user_specification import UserSpecification
from .ads.targ_suggestions_schools import TargSuggestionsSchools
from .ads.client import Client
from .ads.user_specification_cutted import UserSpecificationCutted
from .ads.lookalike_request_save_audience_level import LookalikeRequestSaveAudienceLevel
from .ads.demostats_format import DemostatsFormat
from .ads.musician import Musician
from .ads.stats_sex import StatsSex
from .ads.target_group import TargetGroup
from .ads.stats import Stats
from .ads.link_status import LinkStatus
from .ads.account import Account
from .ads.accesses import Accesses
from .ads.criteria import Criteria
from .ads.stats_sex_age import StatsSexAge
from .ads.create_ad_status import CreateAdStatus
from .ads.create_campaign_status import CreateCampaignStatus
from .ads.users import Users
from .ads.promoted_post_reach import PromotedPostReach
from .ads.stats_format import StatsFormat
from .ads.lookalike_request import LookalikeRequest
from .ads.demo_stats import DemoStats
from .ads.paragraphs import Paragraphs
from .ads.targ_stats import TargStats
from .ads.targ_suggestions_regions import TargSuggestionsRegions
from .ads.rules import Rules
from .ads.stats_age import StatsAge
from .ads.ad import Ad
from .ads.targ_suggestions_cities import TargSuggestionsCities
from .ads.category import Category
from .ads.stats_cities import StatsCities
from .ads.flood_stats import FloodStats
from .ads.targ_suggestions import TargSuggestions
from .storage.value import Value
from .wall.wallpost_attachment import WallpostAttachment
from .wall.wallpost import Wallpost
from .wall.wall_comment import WallComment
from .wall.carousel_base import CarouselBase
from .wall.graffiti import Graffiti
from .wall.wall_comment_donut import WallCommentDonut
from .wall.wallpost_to_id import WallpostToId
from .wall.attached_note import AttachedNote
from .wall.posted_photo import PostedPhoto
from .wall.post_copyright import PostCopyright
from .wall.wallpost_donut_placeholder import WallpostDonutPlaceholder
from .wall.comment_attachment import CommentAttachment
from .wall.wallpost_comments_donut_placeholder import WallpostCommentsDonutPlaceholder
from .wall.views import Views
from .wall.wallpost_full import WallpostFull
from .wall.wall_comment_donut_placeholder import WallCommentDonutPlaceholder
from .wall.wallpost_donut import WallpostDonut
from .wall.app_post import AppPost
from .wall.post_source import PostSource
from .wall.wallpost_comments_donut import WallpostCommentsDonut
from .wall.geo import Geo
from .polls.voters_users import VotersUsers
from .polls.voters import Voters
from .polls.background import Background
from .polls.poll import Poll
from .polls.answer import Answer
from .polls.friend import Friend

__all__ = (
    "AppWidgetsPhotos",
    "PrettyCardsPrettyCard",
    "BaseLinkApplicationStore",
    "AdswebGetFraudHistoryResponseEntriesEntry",
    "PodcastCover",
    "LinkTargetObject",
    "BaseObjectWithName",
    "BaseError",
    "LeadFormsQuestionItem",
    "BaseStickerOld",
    "BaseLikes",
    "PodcastExternalData",
    "StickersImageSet",
    "BaseLinkButtonAction",
    "CommentThread",
    "BaseObject",
    "LeadFormsLead",
    "EventsEventAttach",
    "AppWidgetsPhoto",
    "BaseCity",
    "BaseLinkApplication",
    "BaseLinkRating",
    "LeadFormsAnswerItem",
    "BaseCommentsInfo",
    "ClientInfoForBots",
    "LeadFormsForm",
    "LeadFormsAnswer",
    "BaseStickerAnimation",
    "BaseGradientPoint",
    "BaseUserId",
    "AdswebGetSitesResponseSitesSite",
    "BasePlace",
    "BaseCropPhotoRect",
    "OauthError",
    "BaseRequestParam",
    "BaseLinkProduct",
    "BaseLikesInfo",
    "BaseCropPhoto",
    "BaseGeoCoordinates",
    "BaseRepostsInfo",
    "OwnerState",
    "AudioAudio",
    "AdswebGetStatisticsResponseItemsItem",
    "BaseImage",
    "BaseStickerNew",
    "BaseCropPhotoCrop",
    "BaseLinkButton",
    "BaseLink",
    "AdswebGetAdCategoriesResponseCategoriesCategory",
    "BaseLinkProductCategory",
    "BaseMessageError",
    "BaseUploadServer",
    "BaseGeo",
    "AdswebGetAdUnitsResponseAdUnitsAdUnit",
    "BaseObjectCount",
    "LeadFormsQuestionItemOption",
    "BaseCountry",
    "Participants",
    "Call",
    "DocTypes",
    "DocPreviewAudioMsg",
    "DocPreviewPhoto",
    "DocPreviewPhotoSizes",
    "DocPreview",
    "DocPreviewGraffiti",
    "DocPreviewVideo",
    "Doc",
    "DonatorSubscriptionInfo",
    "Hint",
    "MarketCategory",
    "MarketCategoryNested",
    "Order",
    "MarketCategoryTree",
    "Currency",
    "Section",
    "MarketAlbum",
    "MarketItem",
    "Price",
    "OrderItem",
    "LiveSettings",
    "VideoFiles",
    "LiveInfo",
    "VideoAlbum",
    "VideoFull",
    "Video",
    "SaveResult",
    "VideoImage",
    "Order",
    "Subscription",
    "AmountItem",
    "Amount",
    "Status",
    "ItemVideoVideo",
    "ItemPhotoTagPhotoTags",
    "ItemWallpostFeedbackAnswer",
    "ItemAudioAudio",
    "ItemDigestButton",
    "ItemBase",
    "ItemDigestHeader",
    "NewsfeedPhoto",
    "ItemHolidayRecommendationsBlockHeader",
    "ItemWallpostFeedback",
    "ItemPromoButtonAction",
    "ItemPromoButtonImage",
    "ItemPhotoPhotos",
    "ItemDigestFooter",
    "FeedList",
    "ItemDigestFullItem",
    "ItemFriendFriends",
    "MutualFriend",
    "FriendsList",
    "RequestsXtrMessage",
    "RequestsMutual",
    "Requests",
    "FriendStatus",
    "WikipageHistory",
    "WikipageFull",
    "Wikipage",
    "CountersGroup",
    "GroupsArray",
    "CallbackServer",
    "Address",
    "AddressTimetableDay",
    "Cover",
    "SubjectItem",
    "GroupPublicCategoryList",
    "LongPollEvents",
    "LongPollServer",
    "MemberRole",
    "LinksItem",
    "MemberStatusFull",
    "OnlineStatus",
    "LiveCovers",
    "GroupCategoryFull",
    "GroupTag",
    "LongPollSettings",
    "GroupFull",
    "AddressesInfo",
    "TokenPermissionSetting",
    "MemberStatus",
    "CallbackSettings",
    "GroupCategoryType",
    "Group",
    "GroupAttach",
    "BanInfo",
    "SettingsTwitter",
    "GroupBanInfo",
    "MarketInfo",
    "GroupCategory",
    "OwnerXtrBanInfo",
    "PhotoSize",
    "ContactsItem",
    "AddressTimetable",
    "Activity",
    "Country",
    "Period",
    "City",
    "Reach",
    "SexAge",
    "WallpostStat",
    "Views",
    "NoteComment",
    "Note",
    "Gift",
    "Layout",
    "SendMessageError",
    "SendMessageItem",
    "Notification",
    "Reply",
    "Feedback",
    "NotificationsComment",
    "School",
    "UserXtrType",
    "University",
    "Military",
    "UserSettingsXtr",
    "LastSeen",
    "Occupation",
    "UserMin",
    "Relative",
    "Exports",
    "Career",
    "Personal",
    "OnlineInfo",
    "User",
    "UsersArray",
    "UserCounters",
    "UserConnections",
    "UserFull",
    "School",
    "University",
    "Station",
    "Region",
    "Faculty",
    "Photo",
    "TagsSuggestionItem",
    "PhotoSizes",
    "TagsSuggestionItemButton",
    "PhotoAlbumFull",
    "PhotoFullXtrRealOffset",
    "PhotoUpload",
    "PhotoAlbum",
    "PhotoTag",
    "PhotoXtrTagInfo",
    "Image",
    "PhotoXtrRealOffset",
    "StickersKeywordSticker",
    "StickersKeyword",
    "Product",
    "WidgetPage",
    "WidgetLikes",
    "CommentMedia",
    "CommentReplies",
    "WidgetComment",
    "CommentRepliesItem",
    "Topic",
    "TopicComment",
    "Tag",
    "Page",
    "Bookmark",
    "FeedItem",
    "PromoBlock",
    "StoryStats",
    "StatLine",
    "StoryStatsStat",
    "ClickableArea",
    "ClickableSticker",
    "StoryLink",
    "Replies",
    "ClickableStickers",
    "ViewersItem",
    "Story",
    "SetCounterItem",
    "Transaction",
    "GiveEventStickerItem",
    "Level",
    "TokenChecked",
    "SmsNotification",
    "LinkStats",
    "LinkChecked",
    "Stats",
    "StatsExtended",
    "LinkStatsExtended",
    "DomainResolved",
    "StatsSexAge",
    "StatsCity",
    "ShortLink",
    "LastShortenedLink",
    "StatsCountry",
    "PushParams",
    "Offer",
    "PushConversations",
    "NameRequest",
    "PushSettings",
    "AccountCounters",
    "Info",
    "UserSettingsInterest",
    "UserSettingsInterests",
    "PushConversationsItem",
    "MessagesArray",
    "MessageActionPhoto",
    "KeyboardButtonActionOpenPhoto",
    "Forward",
    "MessageRequestData",
    "LongpollMessages",
    "Chat",
    "LongpollParams",
    "PinnedMessage",
    "AudioMessage",
    "Conversation",
    "ForeignMessage",
    "HistoryAttachment",
    "SendUserIdsResponseItem",
    "ChatSettingsPhoto",
    "Graffiti",
    "PushSettings",
    "KeyboardButtonActionText",
    "ChatSettings",
    "MessageAction",
    "ChatRestrictions",
    "MessageAttachment",
    "ChatSettingsAcl",
    "ConversationPeer",
    "OutReadBy",
    "KeyboardButtonActionOpenLink",
    "ConversationWithMessage",
    "KeyboardButtonActionLocation",
    "ChatPushSettings",
    "ChatFull",
    "GetConversationMembers",
    "Message",
    "Keyboard",
    "ChatSettingsPermissions",
    "LastActivity",
    "KeyboardButtonActionCallback",
    "KeyboardButtonActionVkpay",
    "ConversationSortId",
    "ChatPreview",
    "KeyboardButtonPropertyAction",
    "KeyboardButton",
    "GetConversationById",
    "ConversationCanWrite",
    "HistoryMessageAttachment",
    "ConversationMember",
    "UserXtrInvitedBy",
    "KeyboardButtonActionOpenApp",
    "App",
    "Scope",
    "CatalogList",
    "Leaderboard",
    "AppMin",
    "Campaign",
    "StatsViewsTimes",
    "UpdateOfficeUsersResult",
    "AdLayout",
    "RejectReason",
    "UserSpecification",
    "TargSuggestionsSchools",
    "Client",
    "UserSpecificationCutted",
    "LookalikeRequestSaveAudienceLevel",
    "DemostatsFormat",
    "Musician",
    "StatsSex",
    "TargetGroup",
    "Stats",
    "LinkStatus",
    "Account",
    "Accesses",
    "Criteria",
    "StatsSexAge",
    "CreateAdStatus",
    "CreateCampaignStatus",
    "Users",
    "PromotedPostReach",
    "StatsFormat",
    "LookalikeRequest",
    "DemoStats",
    "Paragraphs",
    "TargStats",
    "TargSuggestionsRegions",
    "Rules",
    "StatsAge",
    "Ad",
    "TargSuggestionsCities",
    "Category",
    "StatsCities",
    "FloodStats",
    "TargSuggestions",
    "Value",
    "WallpostAttachment",
    "Wallpost",
    "WallComment",
    "CarouselBase",
    "Graffiti",
    "WallCommentDonut",
    "WallpostToId",
    "AttachedNote",
    "PostedPhoto",
    "PostCopyright",
    "WallpostDonutPlaceholder",
    "CommentAttachment",
    "WallpostCommentsDonutPlaceholder",
    "Views",
    "WallpostFull",
    "WallCommentDonutPlaceholder",
    "WallpostDonut",
    "AppPost",
    "PostSource",
    "WallpostCommentsDonut",
    "Geo",
    "VotersUsers",
    "Voters",
    "Background",
    "Poll",
    "Answer",
    "Friend",
)


for _entity_name in __all__:
    _entity = globals()[_entity_name]
    if not hasattr(_entity, "update_forward_refs"):
        continue
    _entity.update_forward_refs(
        **{
            "Optional": Optional,
            "Union": Union,
            "List": List,
            **{k: v for k, v in globals().items() if k in __all__}
        }
    )

del _entity
del _entity_name
