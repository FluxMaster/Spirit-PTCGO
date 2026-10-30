"""STUB: effect not implemented — do not guess mechanics.
Maxie (EX4 #73): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your hand or discard pile for a Pokémon with Team Magma in its name and put it onto your Bench. Treat the new Benched Pokémon as a Basic Pokémon. If it is a Stage 2 Pokémon, put 2 damage counters on that Pokémon.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="3006348b-81f8-5dab-9f15-6d35351216d8",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maxie.Name",
    display_name="Maxie",
    searchable_by=["Maxie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
