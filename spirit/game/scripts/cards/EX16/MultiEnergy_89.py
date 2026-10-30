"""STUB: effect not implemented — do not guess mechanics.
Multi Energy (EX16 #89): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Attach Multi Energy to 1 of your Pokémon. While in play, Multi Energy provides every type of Energy but provides only 1 Energy at a time. (Has no effect other than providing Energy.) Multi Energy provides Colorless Energy when attached to a Pokémon that already has Special Energy cards attached to it.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d6a32eb6-e3ad-5d68-9968-df8c74b24602",
    key="EX16",
    name="Multi Energy",
    display_name="Multi Energy",
    searchable_by=["Multi Energy", "Special"],
    subtypes=["Special"],
    collector_number=89,
    set_code="EX16",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
