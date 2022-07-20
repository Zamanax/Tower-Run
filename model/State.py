from enum import Enum

class State(Enum):
    """
    Enum pour le state des Characters
    Utile presque uniquement pour le rendering
    """

    # Normal States

    IdleLeft = 1
    IdleRight = 2
    AttackLeft = 3
    AttackRight = 4
    RunLeft = 5
    RunRight = 6
    Die = 7

    # Special States (utile presque uniquement que pour le Heros)
    InstantMove = 8
    SpecialMoveRight = 9
    SpecialMoveLeft = 10
    Transform = 11