"""STUB: effect not implemented — do not guess mechanics.
Meteor Falls (EX8 #89): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Each player's Active Evolved Pokémon (excluding Pokémon-ex) can use any attack from its Basic Pokémon or its Stage 1 Evolution card. (You still have to pay for that attack's Energy cost.)
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="a9c287b2-8ce4-57df-b1b7-fa7ddfbfe633",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MeteorFalls.Name",
    display_name="Meteor Falls",
    searchable_by=["Meteor Falls", "Stadium"],
    subtypes=["Stadium"],
    collector_number=89,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
