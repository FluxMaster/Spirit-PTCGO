"""STUB: effect not implemented — do not guess mechanics.
Rocket's Sneak Attack (BASE5 #16): trainer effect stubbed.

Card text:
  - Look at your opponent's hand. If he or she has any Trainer cards, choose 1 of them. Your opponent shuffles that card into his or her deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="38c2c2ae-749d-5f3f-bb8b-85ab5e30693c",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsSneakAttack.Name",
    display_name="Rocket's Sneak Attack",
    searchable_by=["Rocket's Sneak Attack"],
    subtypes=[],
    collector_number=16,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
