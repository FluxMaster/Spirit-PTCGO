"""STUB: effect not implemented — do not guess mechanics.
Darkness Energy (ECARD1 #158): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - If the Pokémon Darkness Energy is attached to does damage with an attack (after applying Weakness and Resistance), the attack does 10 more damage. At the end of every turn, put 1 damage counter on the Pokémon Darkness Energy is attached to, unless it's Darkness or has Dark in its name. Darkness Energy provides Darkness Energy. (Doesn't count as a basic Energy card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="afc3c36b-c875-5e0b-a53a-e0eccf298257",
    key="ECARD1",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=158,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
