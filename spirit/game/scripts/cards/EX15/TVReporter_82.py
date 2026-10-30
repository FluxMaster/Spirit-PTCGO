"""STUB: effect not implemented — do not guess mechanics.
TV Reporter (EX15 #82): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Draw 3 cards. Then discard any 1 card from your hand.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="62b7467d-2557-5e13-af29-cfe72c3c0243",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TVReporter.Name",
    display_name="TV Reporter",
    searchable_by=["TV Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=82,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
