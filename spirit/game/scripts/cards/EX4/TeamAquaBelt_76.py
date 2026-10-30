"""Team Aqua Belt: attach restriction wired; between-turns evolve deferred."""
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import attach_to_team

card = PokemonToolCardDef(
    guid="cd2fc041-274c-5f40-bbbb-df945207e758",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaBelt.Name",
    display_name="Team Aqua Belt",
    searchable_by=["Team Aqua Belt", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=76,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    attach_to=attach_to_team("Team Aqua"),
)
