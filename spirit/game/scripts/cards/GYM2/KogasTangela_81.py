"""STUB: effect not implemented — do not guess mechanics.
Koga's Tangela (GYM2 #81): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ad0de43b-dff4-58c8-8741-834c95d73720",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasTangela.Name",
    display_name="Koga's Tangela",
    searchable_by=["Koga's Tangela", "Basic", "KogasTangela"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=114,
    abilities=[
        Attack(
            title="Sleep Powder",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Grasping Vine",
            game_text="Flip a coin. If heads, draw 2 cards.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)