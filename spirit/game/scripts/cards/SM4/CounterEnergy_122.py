"""STUB: effect not implemented — do not guess mechanics.
Counter Energy (SM4 #122): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - If you have more Prize cards remaining than your opponent, and if this card is attached to a Pokémon that isn't a Pokémon-GX or Pokémon-EX, this card provides every type of Energy but provides only 2 Energy at a time.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="78aeabfd-1bd4-575a-960d-031180c8cd49",
    key="SM4",
    name="Counter Energy",
    display_name="Counter Energy",
    searchable_by=["Counter Energy", "Special"],
    subtypes=["Special"],
    collector_number=122,
    set_code="SM4",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
