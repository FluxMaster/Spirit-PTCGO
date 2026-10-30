"""STUB: effect not implemented — do not guess mechanics.
Magma Energy (EX4 #87): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Magma Energy can be attached only to a Pokémon with Team Magma in its name. Magma Energy provides Fighting and /or Darkness Energy but provides 2 Energy at a time. (Doesn't count as a basic Energy card when not in play and has no other effect than providing Energy.) At the end of your turn, discard Magma Energy.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d39dd7f6-5354-535d-9c96-836c92be088a",
    key="EX4",
    name="Magma Energy",
    display_name="Magma Energy",
    searchable_by=["Magma Energy", "Special"],
    subtypes=["Special"],
    collector_number=87,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
