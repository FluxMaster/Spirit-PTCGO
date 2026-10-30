"""STUB: effect not implemented — do not guess mechanics.
Warp Energy (EX16 #91): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Warp Energy provides Colorless Energy. When you attach this card from your hand to your Active Pokémon, switch that Pokémon with 1 of your Benched Pokémon.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="689f8aa6-3fe6-5b72-9cfe-d50dafa2025e",
    key="EX16",
    name="Warp Energy",
    display_name="Warp Energy",
    searchable_by=["Warp Energy", "Special"],
    subtypes=["Special"],
    collector_number=91,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
