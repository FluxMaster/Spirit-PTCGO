"""STUB: effect not implemented — do not guess mechanics.
Return Label (SM9 #153): trainer effect stubbed.

Card text:
  - Put a card from your opponent's discard pile on the bottom of their deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c60ee87a-7414-5475-ab8f-29dfa49dd9bb",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ReturnLabel.Name",
    display_name="Return Label",
    searchable_by=["Return Label", "Item"],
    subtypes=["Item"],
    collector_number=153,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
