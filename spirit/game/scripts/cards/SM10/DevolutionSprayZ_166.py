"""STUB: effect not implemented — do not guess mechanics.
Devolution Spray Z (SM10 #166): trainer effect stubbed.

Card text:
  - Devolve 1 of your evolved Pokémon by shuffling any number of Evolution cards on it into your deck. (That Pokémon can't evolve this turn.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="cd6aad16-2ac2-5568-a8d3-098477c3d15d",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevolutionSprayZ.Name",
    display_name="Devolution Spray Z",
    searchable_by=["Devolution Spray Z", "Item"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
