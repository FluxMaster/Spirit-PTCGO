"""STUB: effect not implemented — do not guess mechanics.
Healing Field (NEO3 #61): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Once during each player's turn, he or she may flip a coin. If heads, that player removes 2 damage counters from his or her Active Pokémon (1 if it only has 1).
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="88ffd2cc-7c5b-5ddd-80f7-0edc1d5b9370",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HealingField.Name",
    display_name="Healing Field",
    searchable_by=["Healing Field", "Stadium"],
    subtypes=["Stadium"],
    collector_number=61,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
