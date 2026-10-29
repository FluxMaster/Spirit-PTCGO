"""STUB: effect not implemented — do not guess mechanics.
Master Ball (GYM2 #116): trainer effect stubbed.

Card text:
  - Look at 7 cards from the top of your deck. You may choose a Basic Pokémon or Evolution card from those cards, show it to your opponent, then put it into your hand. Shuffle the rest into your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3174f8da-44dc-58e3-9d1b-eca9871f4154",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball"],
    subtypes=[],
    collector_number=116,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
