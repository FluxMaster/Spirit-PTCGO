"""STUB: effect not implemented — do not guess mechanics.
Jirachi-GX (SM11 #79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="92f3fcf4-c07d-500a-ad7a-75cf755cf78f",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JirachiGX.Name",
    display_name="Jirachi-GX",
    searchable_by=["Jirachi-GX", "Basic", "GX", "JirachiGX"],
    subtypes=["Basic", "GX"],
    collector_number=79,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=385,
    abilities=[
        Ability(
            title="Psychic Zone",
            game_text="Don't apply Psychic Weakness when Pok\u00e9mon (both yours and your opponent's) take damage from attacks.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Star Search",
            game_text="Search your deck for an Energy card and attach it to 1 of your Psychic Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Star Shield-GX",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=100,
            # STUB: attack effect not implemented
            effect=protect_next_turn(prevent=True, effects_too=True),
        ),
    ],
)