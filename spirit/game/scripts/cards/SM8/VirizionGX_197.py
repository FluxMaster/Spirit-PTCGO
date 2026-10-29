"""STUB: effect not implemented — do not guess mechanics.
Virizion-GX (SM8 #197): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fe7af1e7-89a8-5b4f-a5a6-51ff2550f83f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VirizionGX.Name",
    display_name="Virizion-GX",
    searchable_by=["Virizion-GX", "Basic", "GX", "VirizionGX"],
    subtypes=["Basic", "GX"],
    collector_number=197,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=640,
    abilities=[
        Attack(
            title="Double Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sensitive Blade",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Breeze Away-GX",
            game_text="Put any number of your Pok\u00e9mon in play and all cards attached to them into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)