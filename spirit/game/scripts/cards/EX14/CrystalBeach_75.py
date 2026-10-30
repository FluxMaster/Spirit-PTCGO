"""STUB: effect not implemented — do not guess mechanics.
Crystal Beach (EX14 #75): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Each Special Energy card that provides 2 or more Energy (both yours and your opponent's) now provides only 1 Colorless Energy. This isn't affected by any Poké-Powers or Poké-Bodies.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="c0f1f75e-b36f-5dfa-ba42-791f4f99283e",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalBeach.Name",
    display_name="Crystal Beach",
    searchable_by=["Crystal Beach", "Stadium"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
