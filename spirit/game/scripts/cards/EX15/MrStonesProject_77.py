"""STUB: effect not implemented — do not guess mechanics.
Mr. Stone's Project (EX15 #77): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for up to 2 basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward. Or, search your discard pile for up to 2 basic Energy cards, show them to your opponent, and put them into your hand.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="405bfbf7-8529-50a7-a5c2-aa09a0d86950",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MrStonesProject.Name",
    display_name="Mr. Stone's Project",
    searchable_by=["Mr. Stone's Project", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
