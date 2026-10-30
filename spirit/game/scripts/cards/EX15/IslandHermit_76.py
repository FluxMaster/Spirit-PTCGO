"""STUB: effect not implemented — do not guess mechanics.
Island Hermit (EX15 #76): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Choose up to 2 of your Prize cards and put them face up. (These cards remain face up for the rest of the game.) Draw 2 cards.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2e00cf9d-cae1-542c-9f08-2b45cd8ea345",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IslandHermit.Name",
    display_name="Island Hermit",
    searchable_by=["Island Hermit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=76,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
