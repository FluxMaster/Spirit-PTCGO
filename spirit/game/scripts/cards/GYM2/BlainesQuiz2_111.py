"""STUB: effect not implemented — do not guess mechanics.
Blaine's Quiz #2 (GYM2 #111): trainer effect stubbed.

Card text:
  - Put a card from your hand face down in front of you. Your opponent guesses whether it is an Energy card, a Trainer card, or a Pokémon (Basic or Evolution) card. Flip the card over. If your opponent guessed right, he or she draws 2 cards. If your opponent guessed wrong, you draw 2 cards. Either way, return the card to your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="35a87a27-b12a-5237-bcda-db283205e1a5",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuiz2.Name",
    display_name="Blaine's Quiz #2",
    searchable_by=["Blaine's Quiz #2"],
    subtypes=[],
    collector_number=111,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
