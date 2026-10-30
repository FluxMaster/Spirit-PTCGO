"""STUB: effect not implemented — do not guess mechanics.
Multi Energy (DP2 #118): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Attach Multi Energy to 1 of your Pokémon. While in play, Multi Energy provides every type of Energy but provides only 1 Energy at a time. (Has no effect other than providing Energy.) Multi Energy provides Colorless Energy when attached to a Pokémon that already has Special Energy cards attached to it.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="49783afe-738c-5a8a-b4e6-09563b25fc8a",
    key="DP2",
    name="Multi Energy",
    display_name="Multi Energy",
    searchable_by=["Multi Energy", "Special"],
    subtypes=["Special"],
    collector_number=118,
    set_code="DP2",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
