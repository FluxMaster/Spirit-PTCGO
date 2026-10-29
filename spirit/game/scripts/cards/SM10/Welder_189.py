"""STUB: effect not implemented — do not guess mechanics.
Welder (SM10 #189): trainer effect stubbed.

Card text:
  - Attach up to 2 Fire Energy cards from your hand to 1 of your Pokémon. If you do, draw 3 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="94ab2c0e-e254-5d26-90ae-ad25737d73bd",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Welder.Name",
    display_name="Welder",
    searchable_by=["Welder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
