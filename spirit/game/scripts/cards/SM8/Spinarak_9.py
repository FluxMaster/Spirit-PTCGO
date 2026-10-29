"""STUB: effect not implemented — do not guess mechanics.
Spinarak (SM8 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cbefbef1-dd51-5a72-8e6d-1e0031829cdf",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    display_name="Spinarak",
    searchable_by=["Spinarak", "Basic", "Spinarak"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=167,
    abilities=[
        Attack(
            title="Spider Scram",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned. Put this Pok\u00e9mon and all cards attached to it in the Lost Zone.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sting",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)