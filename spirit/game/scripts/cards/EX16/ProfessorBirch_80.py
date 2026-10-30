"""STUB: effect not implemented — do not guess mechanics.
Professor Birch (EX16 #80): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Draw cards from your deck until you have 6 cards in your hand.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="6dccea49-7207-52db-b670-d04a53c66105",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBirch.Name",
    display_name="Professor Birch",
    searchable_by=["Professor Birch", "Supporter"],
    subtypes=["Supporter"],
    collector_number=80,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
