"""STUB: effect not implemented — do not guess mechanics.
Brooklet Hill (HF #SV88): trainer effect stubbed.

Card text:
  - Once during each player's turn, that player may search their deck for a Basic Water Pokémon or Basic Fighting Pokémon and, put it onto their Bench, and shuffle their deck.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="5d15b7f6-57be-561f-9616-728860e17a53",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrookletHill.Name",
    display_name="Brooklet Hill",
    searchable_by=["Brooklet Hill", "Stadium"],
    subtypes=["Stadium"],
    collector_number=157,
    set_code="HF",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
