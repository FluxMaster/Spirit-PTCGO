"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Treaty (GYM1 #112): trainer effect stubbed.

Card text:
  - Your opponent chooses 1 of the following: everyone chooses 1 of his or her own Prizes and put it into his or her hand, or you draw a card.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="66d88f43-01aa-573a-88ae-9b7efbe4af1f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesTreaty.Name",
    display_name="Lt. Surge's Treaty",
    searchable_by=["Lt. Surge's Treaty"],
    subtypes=[],
    collector_number=112,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
