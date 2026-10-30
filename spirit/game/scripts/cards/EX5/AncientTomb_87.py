"""STUB: effect not implemented — do not guess mechanics.
Ancient Tomb (EX5 #87): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Don't apply Weakness for all Pokémon in play (excluding Pokémon-ex and Pokémon that has an owner in its name).
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="c9f6d6ad-d4c9-59d8-b8fc-b8effe6caa69",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientTomb.Name",
    display_name="Ancient Tomb",
    searchable_by=["Ancient Tomb", "Stadium"],
    subtypes=["Stadium"],
    collector_number=87,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
