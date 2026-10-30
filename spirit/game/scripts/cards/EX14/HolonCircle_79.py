"""STUB: effect not implemented — do not guess mechanics.
Holon Circle (EX14 #79): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Prevent all effects of an attack, including damage, done by either player's Active Pokémon. If an Active Pokémon uses an attack, that attack ends, and discard this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="d6e83b9b-8fce-5f14-bf59-35ad8e4b809d",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonCircle.Name",
    display_name="Holon Circle",
    searchable_by=["Holon Circle", "Stadium"],
    subtypes=["Stadium"],
    collector_number=79,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
