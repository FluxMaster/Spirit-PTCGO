"""STUB: effect not implemented — do not guess mechanics.
Cyclone Energy (EX16 #90): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Cyclone Energy provides Colorless Energy. When you attach this card from your hand to your Active Pokémon, switch 1 of the Defending Pokémon with 1 of your opponent's Benched Pokémon. Your opponent chooses the Benched Pokémon to switch.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="243cf2a0-6b66-5548-b9d3-65ae824a1452",
    key="EX16",
    name="Cyclone Energy",
    display_name="Cyclone Energy",
    searchable_by=["Cyclone Energy", "Special"],
    subtypes=["Special"],
    collector_number=90,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
