"""STUB: effect not implemented — do not guess mechanics.
Digger (BASE5 #75): trainer effect stubbed.

Card text:
  - Flip a coin. If tails, do 10 damage to your Active Pokémon. If heads, your opponent flips a coin. If tails, your opponent does 10 damage to his or her Active Pokémon. If heads, you flip a coin. Keep doing this until a player gets tails.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="9c522fe8-21c4-5527-bfbb-7ba6471a3be4",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Digger.Name",
    display_name="Digger",
    searchable_by=["Digger", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=75,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
