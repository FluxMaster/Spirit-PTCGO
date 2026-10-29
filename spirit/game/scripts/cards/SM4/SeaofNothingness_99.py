"""STUB: effect not implemented — do not guess mechanics.
Sea of Nothingness (SM4 #99): trainer effect stubbed.

Card text:
  - Special Conditions are not removed when Pokémon (both yours and your opponent's) evolve or devolve.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="04a257d7-809b-512d-abb0-4e7d40f3d244",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SeaofNothingness.Name",
    display_name="Sea of Nothingness",
    searchable_by=["Sea of Nothingness", "Stadium"],
    subtypes=["Stadium"],
    collector_number=99,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
