"""STUB: effect not implemented — do not guess mechanics.
Pokédex HANDY910is (DP1 #111): trainer effect stubbed.

Card text:
  - Look at the top 2 cards of your deck, choose 1 of them, and put it into your hand. Put the other card on the bottom of your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5d41809b-f503-5ebc-a5db-8d07eb58bfea",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokedexHANDY910is.Name",
    display_name="Pokédex HANDY910is",
    searchable_by=["Pok\u00e9dex HANDY910is", "Item"],
    subtypes=["Item"],
    collector_number=111,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
