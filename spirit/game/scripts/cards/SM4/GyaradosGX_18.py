"""STUB: effect not implemented — do not guess mechanics.
Gyarados-GX (SM4 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6d4355ae-b8fd-5d22-82e4-802035b84a7c",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosGX.Name",
    display_name="Gyarados-GX",
    searchable_by=["Gyarados-GX", "Stage 1", "GX", "GyaradosGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=18,
    set_code="SM4",
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
        Attack(
            title="Draconic Disaster",
            game_text="If there is any Stadium card in play, this attack does 100 more damage. Then, discard that Stadium card.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 4},
            damage=100,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dread Storm-GX",
            game_text="Discard an Energy from each of your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)