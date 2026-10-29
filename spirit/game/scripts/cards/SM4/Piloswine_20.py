"""STUB: effect not implemented — do not guess mechanics.
Piloswine (SM4 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb1de76e-c82a-5232-8e35-a3c6a8b2d19c",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    display_name="Piloswine",
    searchable_by=["Piloswine", "Stage 1", "Piloswine"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    family_id=220,
    abilities=[
        Attack(
            title="Stampede",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Rest",
            game_text="This Pok\u00e9mon is now Asleep. Heal 90 damage from it.",
            cost={PokemonTypes.COLORLESS: 4},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)