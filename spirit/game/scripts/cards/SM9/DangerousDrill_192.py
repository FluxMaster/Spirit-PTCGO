"""STUB: effect not implemented — do not guess mechanics.
Dangerous Drill (SM9 #192): trainer effect stubbed.

Card text:
  - You can play this card only if you discard a Darkness Pokémon from your hand.
  - Discard a Pokémon Tool or Special Energy card from 1 of your opponent's Pokémon, or discard any Stadium card in play.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e2576c95-282f-5b91-abb8-dbae0cc31809",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DangerousDrill.Name",
    display_name="Dangerous Drill",
    searchable_by=["Dangerous Drill", "Item"],
    subtypes=["Item"],
    collector_number=192,
    set_code="SM9",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
