"""STUB: effect not implemented — do not guess mechanics.
Blaine's Quiz #3 (GYM2 #112): trainer effect stubbed.

Card text:
  - Put a Basic or Evolution card from your hand face down in front of you and tell your opponent the name of an attack of that card. Your opponent guesses the name of that card. Flip the card over. If your opponent guessed right, he or she draws 3 cards. If your opponent guessed wrong, you draw 3 cards. Either way, return the card to your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d3fd7ce7-6607-59d5-bc72-de33ee0ef2e4",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuiz3.Name",
    display_name="Blaine's Quiz #3",
    searchable_by=["Blaine's Quiz #3"],
    subtypes=[],
    collector_number=112,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
