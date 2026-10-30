from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import crystal_shard_colorless

card = PokemonToolCardDef(
    guid="5410f903-d3c0-5055-8284-ad3a5dcfddde",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalShard.Name",
    display_name="Crystal Shard",
    searchable_by=["Crystal Shard", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=85,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    passive=crystal_shard_colorless(),
)
