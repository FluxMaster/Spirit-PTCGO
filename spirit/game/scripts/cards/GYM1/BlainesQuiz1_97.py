"""STUB: effect not implemented — do not guess mechanics.
Blaine's Quiz #1 (GYM1 #97): trainer effect stubbed.

Card text:
  - Put a Basic Pokémon or Evolution card from your hand face down in front of you and tell your opponent its name. Your opponent guesses the length of that Pokémon. Flip the card over. If your opponent guessed right, he or she draws 2 cards. If your opponent guessed wrong, you draw 2 cards. Either way, return the card to your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0980387e-b82a-5159-9794-b27a35fb763c",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuiz1.Name",
    display_name="Blaine's Quiz #1",
    searchable_by=["Blaine's Quiz #1"],
    subtypes=[],
    collector_number=97,
    set_code="GYM1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
