"""STUB: effect not implemented — do not guess mechanics.
Chip-Chip Ice Axe (SM10 #165): trainer effect stubbed.

Card text:
  - Look at the top 3 cards of your opponent's deck and choose 1 of them. Your opponent shuffles the other cards back into their deck. Then, put the card you chose on top of their deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="06f9d510-ef03-5437-b9bd-5f1e0cfa3d77",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChipChipIceAxe.Name",
    display_name="Chip-Chip Ice Axe",
    searchable_by=["Chip-Chip Ice Axe", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
