from enum import Enum

_multinet_sorts_to_abbreviations = [
    "ent",
    "o",
    "co",
    "d",
    "s",
    "ab",
    "at",
    "oa",
    "na",
    "re",
    "io",
    "ta",
    "mo",
    "ad",
    "as",
    "si",
    "dy",
    "da",
    "dn",
    "st",
    "sd",
    "t",
    "l",
    "md",
    "ql",
    "p",
    "tq",
    "gq",
    "mq",
    "nq",
    "rq",
    "fq",
    "oq",
    "aq",
    "qn",
    "qf",
    "nu",
    "nn",
    "me",
    "m",
    "gr",
    "lg",
    "ng",
    "fe"
]

class MultinetSorts(Enum):
    ENTITY = 0
    OBJECT = 1
    CONCRETE_OBJECT = 2
    DISCRETE_OBJECT = 3
    SUBSTANCE = 4
    ABSTRACT_OBJECT = 5
    ATTRIBUTE = 6
    MEASURABLE_ATTRIBUTE = 7 
    NON_MEASURABLE_ATTRIBUTE = 8
    RELATIONSHIP = 9
    IDEAL_OBJECT = 10
    ABTRACT_TEMPORTAL_OBJECT = 11
    MODALITY = 12
    DYNAMIC_SITUATIONAL_OBJECT = 13
    STATIC_SITUATIONAL_OBJECT = 14
    SITUATION = 15
    DYNAMIC_SITUATIONAL = 16
    ACTION = 17
    HAPPENING = 18
    STATIC_SITUATION = 19
    SITUATIONAL_DESCRIPTOR = 20
    TIME = 21
    LOCATION = 22
    MODAL_SITUATIONAL_DESCRIPTOR = 23
    QUALITY = 24
    PROPERTY = 25
    TOTAL_QUALITY = 26
    GRADABLE_QUALITY = 27
    MEASURABLE_QUALITY = 28
    NON_MEASURABLE_QUALITY = 29
    RELATIONAL_QUALITY = 30
    FUNCTIONAL_QUALITY = 31
    OPERATIONAL_QUALITY = 32
    ASSOCIATIVE_QUALITY = 33
    QUANTITY = 34
    QUANTIFICATION = 35
    NUMERICAL_QUANITIFICATOR = 36
    NON_NUMERICAL_QUANTIFICATOR = 37
    UNIT_OF_MEASUREMENT = 38
    MEASUREMENT = 39
    GRADUATOR = 40
    QUALITATIVE_GRADUATOR = 41
    QUANTITATIVE_GRADUATOR = 42
    FORMAL_ENTITY = 43

    def long_name(self):
        return self.name.lower().replace("_"," ")

    def abbreviation(self):
        return _multinet_sorts_to_abbreviations[self.value]

    def __str__(self):
        return self.name
