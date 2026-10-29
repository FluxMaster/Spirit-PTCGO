"""STUB: effect not implemented — do not guess mechanics.
Light Flareon (NEO4 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2d0dc74f-1f8b-5eb5-a135-e135471e6fa0",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightFlareon.Name",
    display_name="Light Flareon",
    searchable_by=["Light Flareon", "Stage 1", "LightFlareon"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=136,
    abilities=[
        Attack(
            title="Warm Up",
            game_text="If you have any benched Pok\u00e9mon, search your deck for a Fire Energy card and attach it to 1 of them. Then shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Burning Flame",
            game_text="Flip 2 coins. For each heads, discard a Fire Energy card attached to Light Flareon or this attack does nothing. This attack does 30 damage plus 20 damage for each heads.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)