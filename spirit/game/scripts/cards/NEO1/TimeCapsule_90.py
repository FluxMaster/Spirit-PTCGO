"""STUB: effect not implemented — do not guess mechanics.
Time Capsule (NEO1 #90): trainer effect stubbed.

Card text:
  - Your opponent may choose 5 Basic Pokémon, Evolution, and/or basic Energy cards in his or her discard pile. (If your opponent doesn't have that many, he or she chooses all or none of them.) If your opponent chooses any cards, he or she shuffles them into his or her deck. Either way, you may do the same, and you can't play any more Trainer cards this turn.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c0f99755-400f-5af7-b06f-e74de09c7a56",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TimeCapsule.Name",
    display_name="Time Capsule",
    searchable_by=["Time Capsule"],
    subtypes=[],
    collector_number=90,
    set_code="NEO1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
