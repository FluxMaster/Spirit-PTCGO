"""Team Magma Belt: attach restriction wired; between-turns evolve deferred."""
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import attach_to_team

card = PokemonToolCardDef(
    guid="d7e857d0-9148-532f-8e60-72576f99906e",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaBelt.Name",
    display_name="Team Magma Belt",
    searchable_by=["Team Magma Belt", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=81,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    attach_to=attach_to_team("Team Magma"),
)
