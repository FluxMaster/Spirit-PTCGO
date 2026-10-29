"""STUB: effect not implemented — do not guess mechanics.
Victreebel (SM10 #15): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2e66586c-bda2-5d16-a5a5-d79753af66b0",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name",
    display_name="Victreebel",
    searchable_by=["Victreebel", "Stage 2", "Victreebel"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Reactive Poison",
            game_text="This attack does 60 more damage for each Special Condition affecting your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gastro Acid",
            game_text="The Defending Pok\u00e9mon has no Abilities until the end of your next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)