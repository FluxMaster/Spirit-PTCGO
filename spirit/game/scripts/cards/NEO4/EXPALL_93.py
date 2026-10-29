"""STUB: effect not implemented — do not guess mechanics.
EXP.ALL (NEO4 #93): trainer effect stubbed.

Card text:
  - Attach EXP.ALL to 1 of your Pokémon that doesn't have a Pokémon Tool attached to it.
  - During your opponent's turn, if your Active Pokémon would be Knocked Out by your opponent's attack, you may take 1 of the basic Energy cards attached to your Active Pokémon and attach it to the Pokémon with EXP.ALL attached to it. If you do, discard EXP.ALL.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="d9d5a4d1-738d-5b47-81de-9e3e2e52e3bc",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EXPALL.Name",
    display_name="EXP.ALL",
    searchable_by=["EXP.ALL", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=93,
    set_code="NEO4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
