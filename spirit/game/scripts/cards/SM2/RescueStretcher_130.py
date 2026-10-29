"""STUB: effect not implemented — do not guess mechanics.
Rescue Stretcher (SM2 #130): trainer effect stubbed.

Card text:
  - Choose 1:
• Put a Pokémon from your discard pile into your hand.
• Shuffle 3 Pokémon from your discard pile into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8f36a4cb-83a1-56a5-b674-68bc025c73db",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueStretcher.Name",
    display_name="Rescue Stretcher",
    searchable_by=["Rescue Stretcher", "Item"],
    subtypes=["Item"],
    collector_number=130,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
