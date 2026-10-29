"""STUB: effect not implemented — do not guess mechanics.
Old Rod (NEO3 #64): trainer effect stubbed.

Card text:
  - Flip 2 coins. If both are heads, put a Baby Pokémon, Basic Pokémon, or Evolution card from your discard pile into your hand. If both are tails, put a Trainer card from your discard pile into your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1d88c3b4-8160-5e7b-9a57-21c661c71984",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldRod.Name",
    display_name="Old Rod",
    searchable_by=["Old Rod"],
    subtypes=[],
    collector_number=64,
    set_code="NEO3",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
