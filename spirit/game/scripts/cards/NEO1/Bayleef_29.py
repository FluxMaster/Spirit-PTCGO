"""STUB: effect not implemented — do not guess mechanics.
Bayleef (NEO1 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a5a0f00-3d1c-5bd1-a7ff-08ba007073e5",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    display_name="Bayleef",
    searchable_by=["Bayleef", "Stage 1", "Bayleef"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name",
    family_id=152,
    abilities=[
        Attack(
            title="Sweet Scent",
            game_text="Flip a coin. If heads and if any of your Pok\u00e9mon have any damage counters on them, then remove 2 damage counters from 1 of them (or 1 if it only has 1). If tails and if any of your opponent's Pok\u00e9mon have any damage counters on them, choose 1 of them and remove 2 damage counters from it (or 1 if it only has 1).",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Double Razor Leaf",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 3},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)