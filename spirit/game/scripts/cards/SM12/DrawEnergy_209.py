"""STUB: effect not implemented — do not guess mechanics.
Draw Energy (SM12 #209): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - When you attach this card from your hand to a Pokémon, draw a card.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="7c7935a3-d73a-522c-bf46-4526b76fc27c",
    key="SM12",
    name="Draw Energy",
    display_name="Draw Energy",
    searchable_by=["Draw Energy", "Special"],
    subtypes=["Special"],
    collector_number=209,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
