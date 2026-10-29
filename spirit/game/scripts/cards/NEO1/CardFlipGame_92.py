"""STUB: effect not implemented — do not guess mechanics.
Card-Flip Game (NEO1 #92): trainer effect stubbed.

Card text:
  - Choose 1 of your opponent's face-down Prizes. Guess whether it is an Energy card, a Trainer card, or a Pokémon (Basic or Evolution) card. Flip the card face up (and leave it face up). If you guessed right, draw 2 cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c32d115b-99f9-5088-b666-b13c677efff8",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CardFlipGame.Name",
    display_name="Card-Flip Game",
    searchable_by=["Card-Flip Game", "Goldenrod Game Corner"],
    subtypes=["Goldenrod Game Corner"],
    collector_number=92,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
