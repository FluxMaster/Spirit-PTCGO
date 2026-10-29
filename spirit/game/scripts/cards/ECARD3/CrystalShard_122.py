"""STUB: effect not implemented — do not guess mechanics.
Crystal Shard (ECARD3 #122): trainer effect stubbed.

Card text:
  - Attach Crystal Shard to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - As long as this card is attached to a Pokémon, that Pokémon's type (color) is Colorless. If that Pokémon attacks, discard this card at the end of the turn.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="9dfe7ec3-cfeb-5b78-903f-d67c415ca902",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalShard.Name",
    display_name="Crystal Shard",
    searchable_by=["Crystal Shard", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=122,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
