"""STUB: effect not implemented — do not guess mechanics.
Lycanroc-GX (HF #SV67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="55f586b9-c428-50c8-b442-86566cb9fc64",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocGX.Name",
    display_name="Lycanroc-GX",
    searchable_by=["Lycanroc-GX", "Stage 1", "GX", "LycanrocGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=136,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Ability(
            title="Twilight Eyes",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Accelerock",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
        Attack(
            title="Splintered Shards-GX",
            game_text="This attack does 30 damage for each Energy card in your opponent's discard pile. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)