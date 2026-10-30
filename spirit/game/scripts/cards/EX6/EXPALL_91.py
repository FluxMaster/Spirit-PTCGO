"""STUB: effect not implemented — do not guess mechanics.
EXP.ALL (EX6 #91): trainer effect stubbed.

Card text:
  - Attach EXP. ALL to 1 of your Pokémon (excluding Pokémon-ex and Pokémon that has an owner in its name) that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - During your opponent's turn, if 1 of your Active Pokémon is Knocked Out by your opponent's attack, you may take 1 basic Energy card attached to that Knocked Out Pokémon and attach it to the Pokémon with EXP.ALL attached to it. If you do, discard EXP.ALL.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="89b46eb3-469d-54ba-9b84-154d808a71c6",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EXPALL.Name",
    display_name="EXP.ALL",
    searchable_by=["EXP.ALL", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=91,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
