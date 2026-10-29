"""STUB: effect not implemented — do not guess mechanics.
Draw Energy (SM12 #271): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - When you attach this card from your hand to a Pokémon, draw a card.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="9a07c4c8-5d74-5519-8f0c-8fb90a5c3c11",
    key="SM12",
    name="Draw Energy",
    display_name="Draw Energy",
    searchable_by=["Draw Energy", "Special"],
    subtypes=["Special"],
    collector_number=271,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
