"""STUB: effect not implemented — do not guess mechanics.
Tormenting Spray (SM3 #125): trainer effect stubbed.

Card text:
  - Choose a random card from your opponent's hand. Your opponent reveals that card. If it's a Supporter card, discard it.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6957d25d-fda7-5fb4-8096-e34502d64d7d",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TormentingSpray.Name",
    display_name="Tormenting Spray",
    searchable_by=["Tormenting Spray", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
