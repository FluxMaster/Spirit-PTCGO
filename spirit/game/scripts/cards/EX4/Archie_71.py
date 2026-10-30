"""STUB: effect not implemented — do not guess mechanics.
Archie (EX4 #71): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for a Pokémon with Team Aqua in its name and put it onto your Bench. Shuffle your deck afterward. Treat the new Benched Pokémon as a Basic Pokémon. If it is a Stage 2 Pokémon, put 2 damage counters on that Pokémon.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="80e76ab7-4498-54c6-b2e6-6722fa6875e3",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Archie.Name",
    display_name="Archie",
    searchable_by=["Archie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=71,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
