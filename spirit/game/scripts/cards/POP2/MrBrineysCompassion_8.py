"""STUB: effect not implemented — do not guess mechanics.
Mr. Briney's Compassion (POP2 #8): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Choose 1 of your Pokémon in play (excluding Pokémon-ex). Return that Pokémon and all cards attached to it to your hand.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="19d6bada-d5a6-5c40-b604-f2b4854f0674",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MrBrineysCompassion.Name",
    display_name="Mr. Briney's Compassion",
    searchable_by=["Mr. Briney's Compassion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=8,
    set_code="POP2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
