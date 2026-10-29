"""STUB: effect not implemented — do not guess mechanics.
Mysterious Treasure (SM6 #113a): trainer effect stubbed.

Card text:
  - Discard a card from your hand. If you do, search your deck for a Psychic or Dragon Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2761d4f0-f0a0-56fc-8aed-90ffc37a4d80",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousTreasure.Name",
    display_name="Mysterious Treasure",
    searchable_by=["Mysterious Treasure", "Item"],
    subtypes=["Item"],
    collector_number=150,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
