"""STUB: effect not implemented — do not guess mechanics.
Electromagnetic Radar (SM10 #169): trainer effect stubbed.

Card text:
  - You can play this card only if you discard 2 other cards from your hand.
  - Search your deck for up to 2 in any combination of Lightning Pokémon-GX and Lightning Pokémon-EX, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ec5d5ca1-5657-5a33-9f80-59e78075246c",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElectromagneticRadar.Name",
    display_name="Electromagnetic Radar",
    searchable_by=["Electromagnetic Radar", "Item"],
    subtypes=["Item"],
    collector_number=169,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
