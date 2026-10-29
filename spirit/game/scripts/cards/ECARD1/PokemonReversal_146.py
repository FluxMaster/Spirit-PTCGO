"""STUB: effect not implemented — do not guess mechanics.
Pokémon Reversal (ECARD1 #146): trainer effect stubbed.

Card text:
  - Choose 1 of your opponent's Benched Pokémon. Flip a coin. If heads, switch that Pokémon with the Defending Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f97bcd3a-7386-5f0e-a5c4-3cb20f8c858c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonReversal.Name",
    display_name="Pokémon Reversal",
    searchable_by=["Pok\u00e9mon Reversal"],
    subtypes=[],
    collector_number=146,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
