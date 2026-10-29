"""STUB: effect not implemented — do not guess mechanics.
Shuckle-GX (SM8 #215): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="b8503192-4084-544e-8722-ec94414af762",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShuckleGX.Name",
    display_name="Shuckle-GX",
    searchable_by=["Shuckle-GX", "Basic", "GX", "ShuckleGX"],
    subtypes=["Basic", "GX"],
    collector_number=215,
    set_code="SM8",
    rarity=Rarities.RareRainbow,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=213,
    abilities=[
        Ability(
            title="Protective Shell",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon that have 2 or fewer Energy attached to them.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Triple Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 3 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Wrap-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)