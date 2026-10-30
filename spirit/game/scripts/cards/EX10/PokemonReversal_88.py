"""STUB: effect not implemented — do not guess mechanics.
Pokémon Reversal (EX10 #88): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, choose 1 of your opponent's Benched Pokémon and switch it with 1 of the Defending Pokémon. Your opponent chooses the Defending Pokémon to switch.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c090317e-e946-50aa-9935-40bb7fbdf094",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonReversal.Name",
    display_name="Pokémon Reversal",
    searchable_by=["Pok\u00e9mon Reversal", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
