"""STUB: effect not implemented — do not guess mechanics.
Holon Energy FF (EX11 #104): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Holon Energy FF provides Colorless Energy.
  - If the Pokémon that Holon Energy FF is attached to also has a basic Fire Energy card attached to it, that Pokémon has no Weakness. If the Pokémon that Holon Energy FF is attached to also has a basic Fighting Energy card attached to it, damage done by that Pokémon's attack isn't affected by Resistance. Ignore these effects if Holon Energy FF is attached to Pokémon-ex.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="0f2eb03f-7fb1-5ac2-be23-cfd5facb9a59",
    key="EX11",
    name="Holon Energy FF",
    display_name="Holon Energy FF",
    searchable_by=["Holon Energy FF", "Special"],
    subtypes=["Special"],
    collector_number=104,
    set_code="EX11",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
