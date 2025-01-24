from enum import StrEnum


class LeadFormsQuestionItemType(StrEnum):
    """ LeadFormsQuestionItemType enum """

    INPUT = "input"
    TEXTAREA = "textarea"
    RADIO = "radio"
    CHECKBOX = "checkbox"
    SELECT = "select"
