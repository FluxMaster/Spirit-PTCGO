"""STUB: effect not implemented — do not guess mechanics.
Erika's Oddish (GYM2 #70): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9f06719e-f8e1-575c-a0c6-726633dad4f0",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasOddish.Name",
    display_name="Erika's Oddish",
    searchable_by=["Erika's Oddish", "Basic", "ErikasOddish"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=43,
    abilities=[
        Attack(
            title="Strange Powder",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused; if tails, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)