"""STUB: effect not implemented — do not guess mechanics.
Great Catcher (SM12 #264): trainer effect stubbed.

Card text:
  - You can play this card only if you discard 2 other cards from your hand.
  - Switch 1 of your opponent's Benched Pokémon-GX or Pokémon-EX with their Active Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="34b89b48-244f-5cdf-8036-f1c642f7797d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatCatcher.Name",
    display_name="Great Catcher",
    searchable_by=["Great Catcher", "Item"],
    subtypes=["Item"],
    collector_number=264,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
