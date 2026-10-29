"""STUB: effect not implemented — do not guess mechanics.
Electropower (SM8 #172a): trainer effect stubbed.

Card text:
  - During this turn, your Lightning Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5ac0501b-4682-5255-b24f-744b6dcddaa2",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Electropower.Name",
    display_name="Electropower",
    searchable_by=["Electropower", "Item"],
    subtypes=["Item"],
    collector_number=237,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
