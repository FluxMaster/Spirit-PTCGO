"""STUB: effect not implemented — do not guess mechanics.
Crystal Shard (EX8 #85): trainer effect stubbed.

Card text:
  - Attach Crystal Shard to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - As long as this card is attached to a Pokémon, that Pokémon's type is Colorless. If that Pokémon attacks, discard this card at the end of the turn.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="5410f903-d3c0-5055-8284-ad3a5dcfddde",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalShard.Name",
    display_name="Crystal Shard",
    searchable_by=["Crystal Shard", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=85,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
