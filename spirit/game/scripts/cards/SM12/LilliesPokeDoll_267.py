"""STUB: effect not implemented — do not guess mechanics.
Lillie's Poké Doll (SM12 #267): trainer effect stubbed.

Card text:
  - Play this card as if it were a 30-HP Colorless Basic Pokémon. At any time during your turn (before your attack), if this Pokémon is your Active Pokémon, you may discard all cards from it and put it on the bottom of your deck.
  - This card can't retreat. If this card is Knocked Out, your opponent can't take any Prize cards for it.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="805bec0f-66ad-5d93-91db-eb373825c1dd",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesPokeDoll.Name",
    display_name="Lillie's Poké Doll",
    searchable_by=["Lillie's Pok\u00e9 Doll", "Item"],
    subtypes=["Item"],
    collector_number=267,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
