"""STUB: effect not implemented — do not guess mechanics.
Scizor-GX (SM7 #158): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="96611c5a-5ad8-5df5-8b0e-c61e159d7a4e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorGX.Name",
    display_name="Scizor-GX",
    searchable_by=["Scizor-GX", "Stage 1", "GX", "ScizorGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=158,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Ability(
            title="Danger Perception",
            game_text="If this Pok\u00e9mon's remaining HP is 100 or less, its attacks do 80 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cross-Cut-GX",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 100 more damage. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)