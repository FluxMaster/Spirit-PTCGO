"""STUB: effect not implemented — do not guess mechanics.
Altar of the Moone (SM2 #117): trainer effect stubbed.

Card text:
  - The Retreat Cost of each Pokémon (both yours and your opponent's) that has any Psychic or Darkness Energy attached to it is ColorlessColorless less.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="b1d91432-5568-55f2-bd79-723bd0422afe",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AltaroftheMoone.Name",
    display_name="Altar of the Moone",
    searchable_by=["Altar of the Moone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=117,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
