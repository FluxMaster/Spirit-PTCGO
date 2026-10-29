"""STUB: effect not implemented — do not guess mechanics.
Tapu Bulu-GX (SM3 #149): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8883ed6b-30d3-58f8-88ce-9228ec992a1e",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuBuluGX.Name",
    display_name="Tapu Bulu-GX",
    searchable_by=["Tapu Bulu-GX", "Basic", "GX", "TapuBuluGX"],
    subtypes=["Basic", "GX"],
    collector_number=149,
    set_code="SM3",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=787,
    abilities=[
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Nature's Judgment",
            game_text="You may discard all Energy from this Pok\u00e9mon. If you do, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tapu Wilderness-GX",
            game_text="Heal all damage from this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)