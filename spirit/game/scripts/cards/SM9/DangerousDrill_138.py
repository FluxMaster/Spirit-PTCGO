"""STUB: effect not implemented — do not guess mechanics.
Dangerous Drill (SM9 #138): trainer effect stubbed.

Card text:
  - You can play this card only if you discard a Darkness Pokémon from your hand.
  - Discard a Pokémon Tool or Special Energy card from 1 of your opponent's Pokémon, or discard any Stadium card in play.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d1f44010-4fbc-5195-be78-de8b65fb1949",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DangerousDrill.Name",
    display_name="Dangerous Drill",
    searchable_by=["Dangerous Drill", "Item"],
    subtypes=["Item"],
    collector_number=138,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
