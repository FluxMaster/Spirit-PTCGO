"""STUB: effect not implemented — do not guess mechanics.
Electromagnetic Radar (SM10 #230): trainer effect stubbed.

Card text:
  - You can play this card only if you discard 2 other cards from your hand.
  - Search your deck for up to 2 in any combination of Lightning Pokémon-GX and Lightning Pokémon-EX, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d91e92fc-a188-52af-910d-c2d639f7d86f",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElectromagneticRadar.Name",
    display_name="Electromagnetic Radar",
    searchable_by=["Electromagnetic Radar", "Item"],
    subtypes=["Item"],
    collector_number=230,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
