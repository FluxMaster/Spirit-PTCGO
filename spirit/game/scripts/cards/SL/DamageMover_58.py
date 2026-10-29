"""STUB: effect not implemented — do not guess mechanics.
Damage Mover (SL #58): trainer effect stubbed.

Card text:
  - Move 3 damage counters from 1 of your Pokémon to another of your Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="dc28221b-6481-5d1c-b2a9-209682844fad",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DamageMover.Name",
    display_name="Damage Mover",
    searchable_by=["Damage Mover", "Item"],
    subtypes=["Item"],
    collector_number=58,
    set_code="SL",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
