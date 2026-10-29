"""STUB: effect not implemented — do not guess mechanics.
Misty & Lorelei (SM12 #199): trainer effect stubbed.

Card text:
  - Search your deck for up to 3 Water Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.
  - When you play this card, you may discard 5 other cards from your hand. If you do, during this turn, your Water Pokémon can use their GX attacks even if you have used your GX attack.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b1b4db87-cec7-5c55-84e9-dc8425cca5ee",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistyLorelei.Name",
    display_name="Misty & Lorelei",
    searchable_by=["Misty & Lorelei", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=199,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
