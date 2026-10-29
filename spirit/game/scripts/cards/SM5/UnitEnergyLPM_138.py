"""STUB: effect not implemented — do not guess mechanics.
Unit Energy {L}{P}{M} (SM5 #138): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - While this card is attached to a Pokémon, it provides Lightning, Psychic, and Metal Energy but provides only 1 Energy at a time.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f9104671-a5c1-5eb6-b0fe-fad555549982",
    key="SM5",
    name="Unit Energy {L}{P}{M}",
    display_name="Unit Energy {L}{P}{M}",
    searchable_by=["Unit Energy {L}{P}{M}", "Special"],
    subtypes=["Special"],
    collector_number=138,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
