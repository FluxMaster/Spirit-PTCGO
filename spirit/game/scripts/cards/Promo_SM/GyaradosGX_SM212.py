"""STUB: effect not implemented — do not guess mechanics.
Gyarados-GX (Promo_SM #SM212): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1722495a-9cd4-5018-b4f6-e71f7b13ac4a",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosGX.Name",
    display_name="Gyarados-GX",
    searchable_by=["Gyarados-GX", "Stage 1", "GX", "GyaradosGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=212,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=130,
    abilities=[
        Attack(
            title="Dragon Rage",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Hyper Beam-GX",
            game_text="(You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=240,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)