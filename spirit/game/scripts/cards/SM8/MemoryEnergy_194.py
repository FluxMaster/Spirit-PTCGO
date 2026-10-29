"""STUB: effect not implemented — do not guess mechanics.
Memory Energy (SM8 #194): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - The Pokémon this card is attached to can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f72469c6-2c68-59fa-9d02-d4a610e5a512",
    key="SM8",
    name="Memory Energy",
    display_name="Memory Energy",
    searchable_by=["Memory Energy", "Special"],
    subtypes=["Special"],
    collector_number=194,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
