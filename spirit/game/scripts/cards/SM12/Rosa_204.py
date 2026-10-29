"""STUB: effect not implemented — do not guess mechanics.
Rosa (SM12 #204): trainer effect stubbed.

Card text:
  - You can play this card only if 1 of your Pokémon was Knocked Out during your opponent's last turn.
  - Search your deck for a Pokémon, a Trainer card, and a basic Energy card, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e2e69de4-d96f-5c7c-bb49-5585d70bc83d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rosa.Name",
    display_name="Rosa",
    searchable_by=["Rosa", "Supporter"],
    subtypes=["Supporter"],
    collector_number=204,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
