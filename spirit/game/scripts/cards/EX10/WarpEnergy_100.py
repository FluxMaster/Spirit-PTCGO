"""STUB: effect not implemented — do not guess mechanics.
Warp Energy (EX10 #100): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Warp Energy provides Colorless Energy. When you attach this card from your hand to your Active Pokémon, switch that Pokémon with 1 of your Benched Pokémon.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="560dcc4a-a751-55f6-bda6-38db04a83eeb",
    key="EX10",
    name="Warp Energy",
    display_name="Warp Energy",
    searchable_by=["Warp Energy", "Special"],
    subtypes=["Special"],
    collector_number=100,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
