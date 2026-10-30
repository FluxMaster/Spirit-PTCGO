"""STUB: effect not implemented — do not guess mechanics.
Holon Transceiver (EX11 #98): trainer effect stubbed.

Card text:
  - Search your deck for a Supporter card that has Holon in its name, show it to your opponent, and put it into your hand. Shuffle your deck afterward. Or, search your discard pile for a Supporter card that has Holon in its name, show it to your opponent, and put it into your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="04caf74a-9cd8-5f0e-804e-cea91f974739",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonTransceiver.Name",
    display_name="Holon Transceiver",
    searchable_by=["Holon Transceiver", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
