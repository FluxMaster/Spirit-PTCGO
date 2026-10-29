"""STUB: effect not implemented — do not guess mechanics.
Surprise Box (SM10 #187): trainer effect stubbed.

Card text:
  - Put a card from your opponent's discard pile into their hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="9c5d0692-2693-5f40-8d83-cdc30271655c",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SurpriseBox.Name",
    display_name="Surprise Box",
    searchable_by=["Surprise Box", "Item"],
    subtypes=["Item"],
    collector_number=187,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
