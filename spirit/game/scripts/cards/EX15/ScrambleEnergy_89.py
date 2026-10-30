"""STUB: effect not implemented — do not guess mechanics.
Scramble Energy (EX15 #89): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Scramble Energy can be attached only to an Evolved Pokémon (excluding Pokémon-ex). Scramble Energy provides Colorless Energy. While in play, if you have more Prize cards left than your opponent, Scramble Energy provides every type of Energy but provides only 3 in any combination at a time. If the Pokémon Scramble Energy is attached to isn't an Evolved Pokémon (or evolves into Pokémon-ex), discard Scramble Energy.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4efc5f1e-deba-5ca4-90d2-87e9f17147b6",
    key="EX15",
    name="Scramble Energy",
    display_name="Scramble Energy",
    searchable_by=["Scramble Energy", "Special"],
    subtypes=["Special"],
    collector_number=89,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
