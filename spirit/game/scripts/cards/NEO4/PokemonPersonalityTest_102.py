"""STUB: effect not implemented — do not guess mechanics.
Pokémon Personality Test (NEO4 #102): trainer effect stubbed.

Card text:
  - Put an Evolution card from your hand face down in front of you. Your opponent guesses whether it is a Pokémon card with Light in its name, a Pokémon card with Dark in its name, or neither one. Flip the card over. If your opponent guessed right, he or she draws 3 cards. If your opponent guessed wrong, you draw 3 cards. Either way, return the card to your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="58ef2c6c-602e-55ea-b203-84caaafbe1d8",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonPersonalityTest.Name",
    display_name="Pokémon Personality Test",
    searchable_by=["Pok\u00e9mon Personality Test"],
    subtypes=[],
    collector_number=102,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
