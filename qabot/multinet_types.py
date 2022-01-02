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
    "abs",
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
    CONCRETE_OBJECT = 11
    DISCRETE_OBJECT = 111
    SUBSTANCE = 112
    ABSTRACT_OBJECT = 12
    ATTRIBUTE = 121
    MEASURABLE_ATTRIBUTE = 1211
    NON_MEASURABLE_ATTRIBUTE = 1212
    RELATIONSHIP = 122
    IDEAL_OBJECT = 123
    ABTRACT_TEMPORTAL_OBJECT = 124
    MODALITY = 125
    SITUATIONAL_OBJECT = 126
    DYNAMIC_SITUATIONAL_OBJECT = 1261
    STATIC_SITUATIONAL_OBJECT = 1262
    SITUATION = 2
    DYNAMIC_SITUATIONAL = 21
    ACTION = 211
    HAPPENING = 212
    STATIC_SITUATION = 22
    SITUATIONAL_DESCRIPTOR = 3
    TIME = 31
    LOCATION = 32
    MODAL_SITUATIONAL_DESCRIPTOR = 33
    QUALITY = 4
    PROPERTY = 41
    TOTAL_QUALITY = 411
    GRADABLE_QUALITY = 412
    MEASURABLE_QUALITY = 4121
    NON_MEASURABLE_QUALITY = 4122
    RELATIONAL_QUALITY = 42
    FUNCTIONAL_QUALITY = 43
    OPERATIONAL_QUALITY = 431
    ASSOCIATIVE_QUALITY = 432
    QUANTITY = 5
    QUANTIFICATOR = 51
    NUMERICAL_QUANITIFICATOR = 511
    NON_NUMERICAL_QUANTIFICATOR = 512
    UNIT_OF_MEASUREMENT = 52
    MEASUREMENT = 53
    GRADUATOR = 6
    QUALITATIVE_GRADUATOR = 61
    QUANTITATIVE_GRADUATOR = 62
    FORMAL_ENTITY = 7

    def long_name(self):
        return self.name.lower().replace("_"," ")

    def abbreviation(self):
        return _multinet_sorts_to_abbreviations[self.value]

    def is_subset_of(self, parent):
        # Returns true if this enum is a subset of the passed in enum
        # For example: A discrete object (d) is a subset of object (o)
        if parent.value == 0:
            return True
        if parent.value > self.value: # All children have larger values than their parents
            return False
        # Break down into string and compare by tree
        parent_tree = str(parent.value)
        own_tree = str(self.value)
        for i in range(0,len(parent_tree)):
            if own_tree[i] != parent_tree[i]:
                return False
        
        return True

    def __str__(self):
        return self.name
