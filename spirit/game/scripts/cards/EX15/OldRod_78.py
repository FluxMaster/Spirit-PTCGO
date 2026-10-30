"""STUB: effect not implemented — do not guess mechanics.
Old Rod (EX15 #78): trainer effect stubbed.

Card text:
  - Flip 2 coins. If both are heads, search your discard pile for a Basic Pokémon or Evolution card, show it to your opponent, and put it into your hand. If both are tails, search your discard pile for a Trainer card, show it to your opponent, and put it into your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="31ad4660-f40b-5c53-bace-f47b33c8155c",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldRod.Name",
    display_name="Old Rod",
    searchable_by=["Old Rod", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
