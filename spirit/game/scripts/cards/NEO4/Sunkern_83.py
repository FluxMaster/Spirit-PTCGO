"""STUB: effect not implemented — do not guess mechanics.
Sunkern (NEO4 #83): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="26a0f82e-d3c1-5b2f-afaf-0db26a40f5db",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    display_name="Sunkern",
    searchable_by=["Sunkern", "Basic", "Sunkern"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=191,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Sunbathe",
            game_text="Flip a coin. If heads, remove all damage counters from Sunkern. Search your deck for a card that evolves from Sunkern and attach that card to Sunkern. This counts as evolving Sunkern. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)