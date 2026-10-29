"""STUB: effect not implemented — do not guess mechanics.
Dark Forretress (NEO4 #35): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4ae42081-2705-5af6-8bc8-2ff662cd063a",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkForretress.Name",
    display_name="Dark Forretress",
    searchable_by=["Dark Forretress", "Stage 1", "DarkForretress"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Attack(
            title="Armor Up",
            game_text="Until the end of your next turn, if Dark Forretress would be Knocked Out by damage from an attack, flip a coin. If heads, Dark Forretress is not Knocked Out and its remaining HP become 10 instead.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Explosion",
            game_text="Dark Forretress does 60 damage to itself.",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)