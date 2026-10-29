"""STUB: effect not implemented — do not guess mechanics.
Arcade Game (NEO1 #83): trainer effect stubbed.

Card text:
  - Shuffle your deck, then reveal the top 3 cards of it. If at least 2 of those cards share the same name, put all the ones with that name into your hand and shuffle the rest into your deck. If none of them do, shuffle all 3 into your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="cd37f2ff-8a76-5d83-bb71-24844fa471aa",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArcadeGame.Name",
    display_name="Arcade Game",
    searchable_by=["Arcade Game", "Goldenrod Game Corner"],
    subtypes=["Goldenrod Game Corner"],
    collector_number=83,
    set_code="NEO1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
