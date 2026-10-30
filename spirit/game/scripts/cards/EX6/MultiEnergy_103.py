"""STUB: effect not implemented — do not guess mechanics.
Multi Energy (EX6 #103): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Attach Multi Energy to 1 of your Pokémon. While in play, Multi Energy provides every type of Energy but provides only 1 Energy at a time. (Doesn't count as a basic Energy card when not in play.) Multi Energy provides Colorless Energy when attached to a Pokémon that already has Special Energy cards attached to it.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="06b18a30-413e-5771-b9d1-912cbd5fdbbc",
    key="EX6",
    name="Multi Energy",
    display_name="Multi Energy",
    searchable_by=["Multi Energy", "Special"],
    subtypes=["Special"],
    collector_number=103,
    set_code="EX6",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
