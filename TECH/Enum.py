__author__ = 'PirminVDB'

def enum(**enums):
    return type('Enum', (), enums)

ADDITIVE_PRIMARY_COLOR = enum(R="Red", G="Green", B="Blue")