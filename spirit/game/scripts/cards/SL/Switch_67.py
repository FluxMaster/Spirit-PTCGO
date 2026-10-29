"""STUB: effect not implemented — do not guess mechanics.
Switch (SL #67): trainer effect stubbed.

Card text:
  - Switch your Active Pokémon with 1 of your Benched Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="bdf86208-74f6-568e-abdf-f8fc04fc8623",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=67,
    set_code="SL",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
