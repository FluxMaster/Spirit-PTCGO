"""STUB: effect not implemented — do not guess mechanics.
Rescue Stretcher (SM2 #130a): trainer effect stubbed.

Card text:
  - Choose 1:
• Put a Pokémon from your discard pile into your hand.
• Shuffle 3 Pokémon from your discard pile into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="223ea9a6-01e8-5520-9ed8-ba868ef81245",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueStretcher.Name",
    display_name="Rescue Stretcher",
    searchable_by=["Rescue Stretcher", "Item"],
    subtypes=["Item"],
    collector_number=179,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
