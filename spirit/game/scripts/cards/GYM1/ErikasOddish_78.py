"""STUB: effect not implemented — do not guess mechanics.
Erika's Oddish (GYM1 #78): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d26b4275-2eb4-5300-a506-bd8584e4bff7",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasOddish.Name",
    display_name="Erika's Oddish",
    searchable_by=["Erika's Oddish", "Basic", "ErikasOddish"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=43,
    abilities=[
        Attack(
            title="Blot",
            game_text="If there are any damage counters on Erika's Oddish, remove 1 of them.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sporadic Sponging",
            game_text="If Erika's Oddish has any damage counters on it, flip a coin. If heads, remove 1 of those damage counters.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)