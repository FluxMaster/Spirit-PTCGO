"""STUB: effect not implemented — do not guess mechanics.
Pokédex (BASE4 #115): trainer effect stubbed.

Card text:
  - Look at up to 5 cards from the top of your deck and rearrange them as you like.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b8ddbc72-9ceb-5ecd-bc47-9869b769a3e1",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokedex.Name",
    display_name="Pokédex",
    searchable_by=["Pok\u00e9dex"],
    subtypes=[],
    collector_number=115,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
