"""STUB: effect not implemented — do not guess mechanics.
Mina (SM8 #211): trainer effect stubbed.

Card text:
  - Search your deck for a Fairy Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e29f2542-6657-5fb2-9244-0cfb4b627166",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mina.Name",
    display_name="Mina",
    searchable_by=["Mina", "Supporter"],
    subtypes=["Supporter"],
    collector_number=211,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
