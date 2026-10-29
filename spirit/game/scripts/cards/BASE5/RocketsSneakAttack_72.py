"""STUB: effect not implemented — do not guess mechanics.
Rocket's Sneak Attack (BASE5 #72): trainer effect stubbed.

Card text:
  - Look at your opponent's hand. If he or she has any Trainer cards, choose 1 of them. Your opponent shuffles that card into his or her deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ae3caa63-1d33-5ddd-b7df-0a59799625dd",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsSneakAttack.Name",
    display_name="Rocket's Sneak Attack",
    searchable_by=["Rocket's Sneak Attack"],
    subtypes=[],
    collector_number=72,
    set_code="BASE5",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
