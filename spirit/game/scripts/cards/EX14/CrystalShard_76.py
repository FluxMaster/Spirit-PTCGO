"""STUB: effect not implemented — do not guess mechanics.
Crystal Shard (EX14 #76): trainer effect stubbed.

Card text:
  - Attach Crystal Shard to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - As long as Crystal Shard is attached to a Pokémon, that Pokémon's type is Colorless. If that Pokémon attacks, discard this card at the end of the turn.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="7a50104c-02b9-5e68-b9fe-8f5ba3afa8fa",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalShard.Name",
    display_name="Crystal Shard",
    searchable_by=["Crystal Shard", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=76,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
