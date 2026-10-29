"""STUB: effect not implemented — do not guess mechanics.
Turtwig (SM5 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ab71f31c-6557-5161-811a-cb3e03362f87",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    display_name="Turtwig",
    searchable_by=["Turtwig", "Basic", "Turtwig"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=387,
    abilities=[
        Attack(
            title="Synthesis",
            game_text="Search your deck for a Grass Energy card and attach it to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)