"""STUB: effect not implemented — do not guess mechanics.
Light Sunflora (NEO4 #72): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e1c97f0f-e096-521d-8c3e-5c16e2d28f56",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightSunflora.Name",
    display_name="Light Sunflora",
    searchable_by=["Light Sunflora", "Stage 1", "LightSunflora"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    family_id=191,
    abilities=[
        Attack(
            title="Reflected Sunlight",
            game_text="Attach up to 2 Grass Energy cards from your hand to 1 of your Grass Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 3},
            damage=40,
        ),
    ],
)