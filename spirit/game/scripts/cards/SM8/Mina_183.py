"""STUB: effect not implemented — do not guess mechanics.
Mina (SM8 #183): trainer effect stubbed.

Card text:
  - Search your deck for a Fairy Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c94e3145-336b-5f21-b872-42b564179c00",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mina.Name",
    display_name="Mina",
    searchable_by=["Mina", "Supporter"],
    subtypes=["Supporter"],
    collector_number=183,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
