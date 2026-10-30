"""STUB: effect not implemented — do not guess mechanics.
Holon Lass (EX11 #92): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Discard a card from your hand. If you can't discard a card from your hand, you can't play this card.
  - Count the total number of Prize cards left (both yours and your opponent's). Look at that many cards from the top of your deck, choose as many Energy cards as you like, show them to your opponent, and put them into your hand. Put the other cards back on top of your deck. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="4b2c9f25-2b86-5a72-9d24-1db56be28bc5",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonLass.Name",
    display_name="Holon Lass",
    searchable_by=["Holon Lass", "Supporter"],
    subtypes=["Supporter"],
    collector_number=92,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
