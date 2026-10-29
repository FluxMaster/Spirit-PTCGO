"""STUB: effect not implemented — do not guess mechanics.
Nightly Garbage Run (BASE5 #77): trainer effect stubbed.

Card text:
  - Choose up to 3 Basic Pokémon cards, Evolution cards, and/or basic Energy cards from your discard pile. Show them to your opponent and shuffle them into your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ed148e61-382d-587f-aeca-e7ff9a5bdda0",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightlyGarbageRun.Name",
    display_name="Nightly Garbage Run",
    searchable_by=["Nightly Garbage Run", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=77,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
