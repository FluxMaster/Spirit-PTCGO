"""STUB: effect not implemented — do not guess mechanics.
Holon Energy GL (EX11 #105): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Holon Energy GL provides Colorless Energy.
  - If the Pokémon that Holon Energy GL is attached to also has a basic Grass Energy card attached to it, that Pokémon can't be affected by any Special Conditions. If the Pokémon that Holon Energy GL is attached to also has a basic Lightning Energy card attached to it, damage done by your opponent's Pokémon-ex is reduced by 10. Ignore these effects if Holon Energy GL is attached to Pokémon-ex.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="e2e59f69-c5b7-5b82-a411-a49732188679",
    key="EX11",
    name="Holon Energy GL",
    display_name="Holon Energy GL",
    searchable_by=["Holon Energy GL", "Special"],
    subtypes=["Special"],
    collector_number=105,
    set_code="EX11",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
