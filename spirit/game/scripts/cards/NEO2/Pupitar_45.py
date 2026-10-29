"""STUB: effect not implemented — do not guess mechanics.
Pupitar (NEO2 #45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e2055332-f46d-5d19-9ef2-1e5cbbac9d3d",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    display_name="Pupitar",
    searchable_by=["Pupitar", "Stage 1", "Pupitar"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Skull Bash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Dust Devil",
            game_text="Does 10 damage to each non-Fighting Pok\u00e9mon in play. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.FIGHTING: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)