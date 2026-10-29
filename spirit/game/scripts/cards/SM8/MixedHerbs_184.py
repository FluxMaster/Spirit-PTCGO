"""STUB: effect not implemented — do not guess mechanics.
Mixed Herbs (SM8 #184): trainer effect stubbed.

Card text:
  - You may play 2 Mixed Herbs cards at once.
• If you played 1 card, remove a Special Condition from your Active Pokémon.
• If you played 2 cards, heal 90 damage and remove all Special Conditions from your Active Pokémon. (This effects works one time for 2 cards.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="61b59328-f41d-5248-b72a-c0fd4ed8217d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MixedHerbs.Name",
    display_name="Mixed Herbs",
    searchable_by=["Mixed Herbs", "Item"],
    subtypes=["Item"],
    collector_number=184,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
