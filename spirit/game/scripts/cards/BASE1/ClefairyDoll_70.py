"""STUB: effect not implemented — do not guess mechanics.
Clefairy Doll (BASE1 #70): trainer effect stubbed.

Card text:
  - Play Clefairy Doll as if it were a Basic Pokémon. While in play, Clefairy Doll counts as a Pokémon (instead of a Trainer card). Clefairy Doll has no attacks, can't retreat, and can't be Asleep, Confused, Paralyzed, or Poisoned. If Clefairy Doll is Knocked Out, it doesn't count as a Knocked Out Pokémon. At any time during your turn before your attack, you may discard Clefairy Doll.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b4047f72-2203-5b26-81ba-b562b7bc009d",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClefairyDoll.Name",
    display_name="Clefairy Doll",
    searchable_by=["Clefairy Doll"],
    subtypes=[],
    collector_number=70,
    set_code="BASE1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
