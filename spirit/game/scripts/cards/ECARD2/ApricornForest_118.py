"""STUB: effect not implemented — do not guess mechanics.
Apricorn Forest (ECARD2 #118): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Once during each player's turn (before attacking), if that player's Bench isn't full, that player flips a coin. If heads, that player shows his or her opponent a basic Energy card from his or her hand. Then, that player searches his or her deck for a Basic Pokémon card of the same type (color) as the revealed Energy card and puts it onto his or her Bench. The player shuffles his or her deck afterward.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="fbac458b-7552-51ee-a3b2-63c9044f60fe",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ApricornForest.Name",
    display_name="Apricorn Forest",
    searchable_by=["Apricorn Forest", "Stadium"],
    subtypes=["Stadium"],
    collector_number=118,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
