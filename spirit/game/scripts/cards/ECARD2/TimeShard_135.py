"""STUB: effect not implemented — do not guess mechanics.
Time Shard (ECARD2 #135): trainer effect stubbed.

Card text:
  - Attach Time Shard to 1 of your Pokémon that doesn't already have a Pokémon Tool card attached to it. If that Pokémon is Knocked Out, discard this card.
  - If the Pokémon this card is attached to is Knocked Out by damage from the Defending Pokémon's attack during your opponent's turn, you may return up to 2 basic Energy cards attached to that Pokémon to your hand.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="6afddc1d-2b79-5aba-96a9-3cb8d4cb33b5",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TimeShard.Name",
    display_name="Time Shard",
    searchable_by=["Time Shard", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=135,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
