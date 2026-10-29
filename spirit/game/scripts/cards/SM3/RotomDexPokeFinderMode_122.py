"""STUB: effect not implemented — do not guess mechanics.
Rotom Dex Poké Finder Mode (SM3 #122): trainer effect stubbed.

Card text:
  - Look at the top 4 cards of your deck and put them back in any order or shuffle them into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="21dff0ef-6275-5b93-b3eb-171cd14943b8",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotomDexPokeFinderMode.Name",
    display_name="Rotom Dex Poké Finder Mode",
    searchable_by=["Rotom Dex Pok\u00e9 Finder Mode", "Item"],
    subtypes=["Item"],
    collector_number=122,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
