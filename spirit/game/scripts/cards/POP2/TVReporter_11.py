"""STUB: effect not implemented — do not guess mechanics.
TV Reporter (POP2 #11): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Draw 3 cards. Then discard any 1 card from your hand.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="89ef67e0-8fe8-5107-a6ce-3cbd3ea62bd9",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TVReporter.Name",
    display_name="TV Reporter",
    searchable_by=["TV Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=11,
    set_code="POP2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
