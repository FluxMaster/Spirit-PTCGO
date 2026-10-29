"""STUB: effect not implemented — do not guess mechanics.
Lysandre Labs (SM6 #111): trainer effect stubbed.

Card text:
  - Pokémon Tool cards in play (both yours and your opponent's) have no effect.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="f885b1a4-7263-52f1-99a1-7d0e9e26edb8",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LysandreLabs.Name",
    display_name="Lysandre Labs",
    searchable_by=["Lysandre Labs", "Stadium"],
    subtypes=["Stadium"],
    collector_number=111,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
