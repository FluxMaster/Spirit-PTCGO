"""STUB: effect not implemented — do not guess mechanics.
Championship Arena (NP #28): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - At the end of each player's turn, if that player has 8 or more cards in his or her hand, that player discards a number of cards until that player has 7 cards left in his or her hand.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="9ee1eb42-ac0d-5d23-b89d-4af5ae9b6022",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionshipArena.Name",
    display_name="Championship Arena",
    searchable_by=["Championship Arena", "Stadium"],
    subtypes=["Stadium"],
    collector_number=28,
    set_code="NP",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
