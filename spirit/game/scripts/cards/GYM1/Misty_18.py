"""STUB: effect not implemented — do not guess mechanics.
Misty (GYM1 #18): trainer effect stubbed.

Card text:
  - Discard 2 of the other cards in your hand in order to play this card. If this turn's attack does damage to the Defending Pokémon (after applying Weakness and Resistance), and if the attacking Pokémon has Misty in its name, the attack does 20 more damage to the Defending Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ef622217-068c-5818-9591-e1f69689b011",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Misty.Name",
    display_name="Misty",
    searchable_by=["Misty"],
    subtypes=[],
    collector_number=18,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
