"""STUB: effect not implemented — do not guess mechanics.
Aqua Energy (EX4 #86): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Aqua Energy can be attached only to a Pokémon with Team Aqua in its name. Aqua Energy provides Water and Darkness Energy but provides 2 Energy at a time. (Doesn't count as a basic Energy card when not in play and has no other effect than providing Energy.) At the end of your turn, discard Aqua Energy.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="09dd569f-37fa-567a-8b4e-662d8927d9e9",
    key="EX4",
    name="Aqua Energy",
    display_name="Aqua Energy",
    searchable_by=["Aqua Energy", "Special"],
    subtypes=["Special"],
    collector_number=86,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
