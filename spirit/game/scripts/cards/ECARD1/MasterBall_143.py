"""STUB: effect not implemented — do not guess mechanics.
Master Ball (ECARD1 #143): trainer effect stubbed.

Card text:
  - Look at 7 cards from the top of your deck. You may choose a Basic Pokémon or Evolution card from those cards, show it your opponent, and put it into your hand. Shuffle the rest into your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ad5cd530-6545-577e-b08a-7cdb6e409f21",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball"],
    subtypes=[],
    collector_number=143,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
