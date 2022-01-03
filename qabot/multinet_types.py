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
        """Returns true if this enum is a subset of the passed in enum
        For example: A discrete object (d) is a subset of object (o)"""
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

    def is_ositl(self):
        """Returns true if the value is an object, situation, time, or location.
        Useful for determining if the node has osi-tl-lay layer information"""
        return is_otl() or is_subset_of(MultinetSorts.SITUATION)

    def is_otl(self):
        """Returns true if the value is an object, time, or location.
        Userful for determining if the node has o-tl-lay layer information"""
        return is_subset_of(MultinetSorts.OBJECT) or is_subset_of(MultinetSorts.TIME) or is_subset_of(MultinetSorts().LOCATION)

    def __str__(self):
        return self.name

class MultinetDetermination(Enum):
    # REFER
    DETERMINATE = 1
    INDETERMINATE = 2

    def abbreviation(self):
        if self.value == MultinetDetermination.DETERMINATE:
            return "det"
        else:
            return "indet"

    def __str__(self):
        return self.name

class MultinetGenerality(Enum):
    # GENER
    SPECIALIZED = 1
    GENERALIZED = 2

    def abbreviation(self):
        if self.value == MultinetGenerality.SPECIALIZED:
            return "sp"
        else:
            return "ge"

    def __str__(self):
        return self.name

class MultinetVariability(Enum):
    # VARIA
    CONSTANT = 1
    VARIABLE = 2
    PLURAL_VARIABLE = 3

    def abbreviation(self):
        if self.value == MultinetVariability.CONSTANT:
            return "const"
        elif self.value == MultinetVariability.PLURAL_VARIABLE:
            return "varia"
        else:
            return "var"

    def __str__(self):
        return self.name

class MultinetFacticity(Enum):
    # FACT
    REAL = 1            # true
    HYPOTHETICAL = 2    # unkown
    NON_REAL = 3        # false

    def abbreviation(self):
        if self.value == MultinetFacticity.REAL:
            return "real"
        elif self.value == MultinetFacticity.HYPOTHETICAL:
            return "hypo"
        else:
            return "non"

    def __str__(self):
        return self.name

class MultinetKType(Enum):
    # K-TYPE
    RESTRICTIVE = 1     # R - restr
    CATEGORICAL = 2     # K - immanent (categorical)
    PROTOTYPICAL = 3    # D - immanent (prototypical)
    SITUATIONAL = 4     # S - situational, assertional + definitional

    def is_immanent(self):
        return self.value == MultinetKType.CATEGORICAL or self.value == MultinetKType.PROTOTYPICAL
    
    def is_descriptive(self):
        return is_immanent() or self.value == MultinetKType.SITUATIONAL

    def __str__(self):
        return self.name