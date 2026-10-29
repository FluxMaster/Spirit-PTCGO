"""STUB: effect not implemented — do not guess mechanics.
Ecogym (NEO1 #84): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Whenever an attack, Pokémon Power, or Trainer card discards another player's non-Colorless Energy card from a Pokémon, return that Energy card to its owner's hand. (Energy cards that are discarded when that Pokémon is Knocked Out don't count.)
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="49d16f73-cbb4-58d7-ad36-fc862a7a73be",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ecogym.Name",
    display_name="Ecogym",
    searchable_by=["Ecogym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=84,
    set_code="NEO1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
