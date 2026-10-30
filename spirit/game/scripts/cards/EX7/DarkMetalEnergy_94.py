"""STUB: effect not implemented — do not guess mechanics.
Dark Metal Energy (EX7 #94): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Attach Dark Metal Energy to 1 of your Pokémon. While in play, Dark Metal Energy provides Darkness Energy and Metal Energy, but provides only 1 Energy at a time. (Doesn't count as a basic Energy card when not in play and has no effect other than providing Energy.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="cde082ce-0988-548a-8c14-55de65d884b6",
    key="EX7",
    name="Dark Metal Energy",
    display_name="Dark Metal Energy",
    searchable_by=["Dark Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=94,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
