"""STUB: effect not implemented — do not guess mechanics.
Misty's Poliwhirl (GYM1 #53): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c4c37128-2a13-538e-8941-71685ab1fcb5",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPoliwhirl.Name",
    display_name="Misty's Poliwhirl",
    searchable_by=["Misty's Poliwhirl", "Stage 1", "MistysPoliwhirl"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPoliwag.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Rapids",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, flip a coin. If heads, choose 1 of those Energy cards and discard it.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Water Punch",
            game_text="Flip a number of coins equal to the number of Water Energy attached to Misty's Poliwhirl. This attack does 30 damage plus 10 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)