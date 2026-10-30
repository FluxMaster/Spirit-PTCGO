"""STUB: effect not implemented — do not guess mechanics.
Swoop! Teleporter (EX7 #92): trainer effect stubbed.

Card text:
  - Search your deck for a Basic Pokémon (excluding Pokémon-ex) and switch it with 1 of your Basic Pokémon (excluding Pokémon-ex) in play. (Any cards attached to that Pokémon, damage counters, Special Conditions, and effects on it are now on the new Pokémon.) Place the first Basic Pokémon in the discard pile. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="950e6cc8-d11f-5e1c-9b36-3a9a78d831ce",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SwoopTeleporter.Name",
    display_name="Swoop! Teleporter",
    searchable_by=["Swoop! Teleporter", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=92,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
