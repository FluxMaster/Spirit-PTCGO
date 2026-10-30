"""STUB: effect not implemented — do not guess mechanics.
Rocket's Mission (EX7 #88): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Discard a card from your hand. Then, draw 3 cards. If you discarded a Pokémon that has Dark or Rocket's in its name, draw 4 cards instead.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="a8128db5-ddf1-564a-bd3b-a1db9276b1e4",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsMission.Name",
    display_name="Rocket's Mission",
    searchable_by=["Rocket's Mission", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
