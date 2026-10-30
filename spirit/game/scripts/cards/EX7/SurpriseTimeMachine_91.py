"""STUB: effect not implemented — do not guess mechanics.
Surprise! Time Machine (EX7 #91): trainer effect stubbed.

Card text:
  - Choose 1 of your Evolved Pokémon, remove the highest Stage Evolution card from it, and shuffle it into your deck (this counts as devolving that Pokémon). If that Pokémon remains in play, search your deck for an Evolution card that evolves from that Pokémon and put it onto that Pokémon (this counts as evolving that Pokémon). Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a37144f2-53be-5d82-989d-42d73e4a4d2b",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SurpriseTimeMachine.Name",
    display_name="Surprise! Time Machine",
    searchable_by=["Surprise! Time Machine", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=91,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
