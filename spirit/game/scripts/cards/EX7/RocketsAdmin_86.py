"""STUB: effect not implemented — do not guess mechanics.
Rocket's Admin. (EX7 #86): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Each player shuffles his or her hand into his or her deck. Then, each player counts his or her Prize cards left and draws up to that many cards. (You draw your cards first.)
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c3c090b0-c699-54e5-ab59-60890a9c6fd6",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsAdmin.Name",
    display_name="Rocket's Admin.",
    searchable_by=["Rocket's Admin.", "Supporter"],
    subtypes=["Supporter"],
    collector_number=86,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
