"""STUB: effect not implemented — do not guess mechanics.
Shrine of Punishment (HF #SV90): trainer effect stubbed.

Card text:
  - Between turns, put 1 damage counter on each Pokémon-GX and Pokémon-EX (both yours and your opponent's).
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="8a45285d-5497-5c7d-b540-9da6304eaca6",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShrineofPunishment.Name",
    display_name="Shrine of Punishment",
    searchable_by=["Shrine of Punishment", "Stadium"],
    subtypes=["Stadium"],
    collector_number=159,
    set_code="HF",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
