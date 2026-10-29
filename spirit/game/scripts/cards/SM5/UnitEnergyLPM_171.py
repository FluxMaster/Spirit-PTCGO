"""STUB: effect not implemented — do not guess mechanics.
Unit Energy {L}{P}{M} (SM5 #171): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - While this card is attached to a Pokémon, it provides Lightning, Psychic, and Metal Energy but provides only 1 Energy at a time.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="a442d5d3-b4ab-5ae9-a6de-246c31e31503",
    key="SM5",
    name="Unit Energy {L}{P}{M}",
    display_name="Unit Energy {L}{P}{M}",
    searchable_by=["Unit Energy {L}{P}{M}", "Special"],
    subtypes=["Special"],
    collector_number=171,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
