"""STUB: effect not implemented — do not guess mechanics.
Minion of Team Rocket (GYM1 #113): trainer effect stubbed.

Card text:
  - Flip 2 coins. If both of them are heads, choose 1 of your opponent's Benched Pokémon and return it and all cards attached to it to his or her hand. If 1 or both of them are tails, your turn ends immediately (you can't attack this turn).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b8630af1-bc33-5a85-b609-2ce96111429d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MinionofTeamRocket.Name",
    display_name="Minion of Team Rocket",
    searchable_by=["Minion of Team Rocket"],
    subtypes=[],
    collector_number=113,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
