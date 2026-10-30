"""STUB: effect not implemented — do not guess mechanics.
Mr. Stone's Project (EX9 #79): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for up to 2 Basic cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward. Or, search your discard pile for up to 2 Basic cards, show them to your opponent, and put them into your hand.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="3ae7468f-1fa1-5ff7-8522-b7e5ba2477b8",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MrStonesProject.Name",
    display_name="Mr. Stone's Project",
    searchable_by=["Mr. Stone's Project", "Supporter"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
