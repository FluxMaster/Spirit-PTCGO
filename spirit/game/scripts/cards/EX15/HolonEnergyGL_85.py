"""STUB: effect not implemented — do not guess mechanics.
Holon Energy GL (EX15 #85): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Holon Energy GL provides Colorless Energy.
  - If the Pokémon that Holon Energy GL is attached to also has a basic Grass Energy card attached to it, that Pokémon can't be affected by any Special Conditions. If the Pokémon that Holon Energy GL is attached to also has a basic Lightning Energy card attached to it, damage done to that Pokémon by attacks from your opponent's Pokémon-ex is reduced by 10. Ignore these effects if Holon Energy GL is attached to Pokémon-ex.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="2d93658b-72f2-5e3f-9075-40ed10ebf019",
    key="EX15",
    name="Holon Energy GL",
    display_name="Holon Energy GL",
    searchable_by=["Holon Energy GL", "Special"],
    subtypes=["Special"],
    collector_number=85,
    set_code="EX15",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
