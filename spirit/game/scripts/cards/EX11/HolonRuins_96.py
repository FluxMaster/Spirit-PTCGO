"""STUB: effect not implemented — do not guess mechanics.
Holon Ruins (EX11 #96): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Each player that has any Pokémon in play that has δ on its card may draw a card once during his or her turn. If the player does, he or she discards a card from his or her hand.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="b6efba11-3e78-5137-97ef-4f0b39e28a3c",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonRuins.Name",
    display_name="Holon Ruins",
    searchable_by=["Holon Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=96,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
