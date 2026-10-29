"""STUB: effect not implemented — do not guess mechanics.
Chaos Gym (GYM2 #102): trainer effect stubbed.

Card text:
  - This card stays in play after being played. Discard this card if another Stadium card comes into play.
  - Whenever a player plays a Trainer card other than a Stadium card, he or she flips a coin. If heads, that player plays that card normally. If tails, the player can't play that card. If the card isn't put into play, the player's opponent may use that card instead, if he or she does everything required in order to play that card (like discarding cards). Either way, the card goes to its owner's discard pile.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="f45119ca-e810-56fa-8944-a81b092242ea",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChaosGym.Name",
    display_name="Chaos Gym",
    searchable_by=["Chaos Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=102,
    set_code="GYM2",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
