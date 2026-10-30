"""STUB: effect not implemented — do not guess mechanics.
Mysterious Shard (EX14 #81): trainer effect stubbed.

Card text:
  - Attach Mysterious Shard to 1 of your Pokémon (excluding Pokémon-ex) that doesn't already have a Pokémon Tool attached to it. If the Pokémon Mysterious Shard is attached to is a Pokémon-ex, discard this card.
  - Prevent all effects of attacks, including damage, done to the Pokémon that Mysterious Shard is attached to by your opponent's Pokémon-ex. Discard this card at the end of your opponent's next turn.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="3d3e002e-1072-5ad8-993d-8a3ab7c9ccd3",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousShard.Name",
    display_name="Mysterious Shard",
    searchable_by=["Mysterious Shard", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=81,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
