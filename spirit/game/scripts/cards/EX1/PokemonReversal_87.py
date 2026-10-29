"""STUB: effect not implemented — do not guess mechanics.
Pokémon Reversal (EX1 #87): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, your opponent switches 1 of his or her Active Pokémon with 1 of his or her Benched Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="06d39a2d-6b7a-5be0-baac-0364c88ebe07",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonReversal.Name",
    display_name="Pokémon Reversal",
    searchable_by=["Pok\u00e9mon Reversal", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
