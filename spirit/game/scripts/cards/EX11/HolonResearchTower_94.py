"""STUB: effect not implemented — do not guess mechanics.
Holon Research Tower (EX11 #94): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Each player's basic Energy cards attached to Pokémon that has δ on its card are both their usual Energy type and Metal type but provide only 1 Energy at a time. (Has no effect other than providing Energy.)
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="d19f95b5-ca44-52b3-8d3a-6fd82c1568ff",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonResearchTower.Name",
    display_name="Holon Research Tower",
    searchable_by=["Holon Research Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
