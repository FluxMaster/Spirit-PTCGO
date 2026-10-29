"""STUB: effect not implemented — do not guess mechanics.
Mallow & Lana (SM12 #231): trainer effect stubbed.

Card text:
  - Switch your Active Pokémon with 1 of your Benched Pokémon.
  - When you play this card, you may discard 2 other cards from your hand. If you do, heal 120 damage from the Pokémon you moved to your Bench.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="d2ddf8ea-890d-57df-a7b8-075d2d50e9df",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MallowLana.Name",
    display_name="Mallow & Lana",
    searchable_by=["Mallow & Lana", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=231,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
