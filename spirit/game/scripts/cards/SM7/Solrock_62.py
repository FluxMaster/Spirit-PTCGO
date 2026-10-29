"""STUB: effect not implemented — do not guess mechanics.
Solrock (SM7 #62): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ae8890a1-d3f2-5696-8ede-af04a95cd9a9",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name",
    display_name="Solrock",
    searchable_by=["Solrock", "Basic", "Solrock"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=338,
    abilities=[
        Ability(
            title="Sunbeam",
            game_text="The maximum HP of each of your Lunatone in play is 130.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Scorching Light",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed. If tails, your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)