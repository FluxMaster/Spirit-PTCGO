"""STUB: effect not implemented — do not guess mechanics.
Wally's Training (EX2 #89): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for a card that evolves from your Active Pokémon (choose 1 if there are 2) and put it on your Active Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="94b26df7-2743-56d6-9c36-aa4d7d250257",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WallysTraining.Name",
    display_name="Wally's Training",
    searchable_by=["Wally's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
