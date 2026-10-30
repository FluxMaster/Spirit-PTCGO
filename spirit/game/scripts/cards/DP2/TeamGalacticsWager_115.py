"""STUB: effect not implemented — do not guess mechanics.
Team Galactic's Wager (DP2 #115): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Each player shuffles his or her hand into his or her deck, and you and your opponent play "Rock-Paper-Scissors." The player who wins draws up to 6 cards. The player who loses draws up to 3 cards. (You draw your cards first.)
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="0f31d040-2705-5e38-86cf-53e7669a73a8",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamGalacticsWager.Name",
    display_name="Team Galactic's Wager",
    searchable_by=["Team Galactic's Wager", "Supporter"],
    subtypes=["Supporter"],
    collector_number=115,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
