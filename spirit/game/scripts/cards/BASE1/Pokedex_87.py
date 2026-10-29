"""STUB: effect not implemented — do not guess mechanics.
Pokédex (BASE1 #87): trainer effect stubbed.

Card text:
  - Look at up to 5 cards from the top of your deck and rearrange them as you like.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="32acf046-cf2f-527e-9d42-a512df600cee",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokedex.Name",
    display_name="Pokédex",
    searchable_by=["Pok\u00e9dex"],
    subtypes=[],
    collector_number=87,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
