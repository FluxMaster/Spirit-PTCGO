"""STUB: effect not implemented — do not guess mechanics.
Celio's Network (EX14 #73): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for a Basic Pokémon or Evolution card (excluding Pokémon-ex), show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="5277953c-a018-5165-9db2-80ef198b7421",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeliosNetwork.Name",
    display_name="Celio's Network",
    searchable_by=["Celio's Network", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
