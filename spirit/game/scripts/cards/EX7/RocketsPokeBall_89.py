"""STUB: effect not implemented — do not guess mechanics.
Rocket's Poké Ball (EX7 #89): trainer effect stubbed.

Card text:
  - Search your deck for a Pokémon with Dark in its name, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1b53536b-8886-56bb-96f2-aa838456c2d5",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsPokeBall.Name",
    display_name="Rocket's Poké Ball",
    searchable_by=["Rocket's Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
