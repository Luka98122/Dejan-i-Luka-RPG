import pygame


class Globals:
    sizeofEverything = 50
    portalsPlaced = [0, 0]
    entityList = []
    portalList = [0, 0]
    currentMap = 0
    events = 0
    screenDimensions = [1920, 1080]
    charDimensions = []
    maxArmor = 1000
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    specialChars = "!\"£$%^&*()-_+=|\}{[]:;@'~#<>?/,."
    print(len(specialChars))
    state = 0
    keys = 0
    numberDimensions = [
        [0, 0],
        [0, 5],
        [0, 11],
        [0, 17],
        [0, 23],
        [0, 29],
        [0, 35],
        [0, 41],
        [0, 47],
        [0, 53],
    ]
    specialCharDimensions = [
        [0, 0, 7],  #!
        [0, 16, 27],  # "
        [0, 36, 59],  # £
        [0, 68, 91],  # $
        [0, 100, 123],  #%
        [0, 132, 155],  # ^
        [0, 164, 191],  # &
        [0, 200, 223],  # *
        [0, 232, 247],  # (
        [0, 256, 271],  # )
        [0, 280, 303],  # -
        [0, 308, 339],  # _
        [0, 344, 367],  # +
        [0, 376, 399],  # =
        [0, 408, 415],  # |
        [1, 0, 23],  # \
        [1, 60, 79],  # }
        [1, 32, 51],  # {
        [1, 88, 103],  # [
        [1, 112, 127],  # ]
        [1, 136, 143],  #:
        [1, 152, 159],  # ;
        [1, 168, 195],  # @
        [1, 204, 211],  #'
        [1, 220, 243],  # ~
        [1, 252, 279],  ##
        [1, 288, 303],  # <
        [1, 312, 327],  # >
        [1, 336, 351],  # ?
        [1, 360, 383],  # /
        [1, 392, 399],  # ,
        [1, 408, 415],  # .
    ]
    print(len(specialCharDimensions))
