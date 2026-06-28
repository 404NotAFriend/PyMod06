#!/usr/bin/env python3

import elements
from ..potions import strength_potion
from alchemy.elements import create_air


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}' and "
        f"'{strength_potion()}' mixed with '{elements.create_fire()}'"
    )
