"""STUB: effect not implemented — do not guess mechanics.
Life Herb (SM7 #180): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, heal 60 damage and remove all Special Conditions from 1 of your Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="bf702ca9-b6b6-5726-b53d-00fb3670569f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name",
    display_name="Life Herb",
    searchable_by=["Life Herb", "Item"],
    subtypes=["Item"],
    collector_number=180,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
