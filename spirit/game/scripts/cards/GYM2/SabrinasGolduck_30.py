"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Golduck (GYM2 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="146e3ddd-4caf-5341-b783-abb68ed118bd",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasGolduck.Name",
    display_name="Sabrina's Golduck",
    searchable_by=["Sabrina's Golduck", "Stage 1", "SabrinasGolduck"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasPsyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Damage Shift",
            game_text="Move 1 damage counter from each of your Pok\u00e9mon that has any on it to the Defending Pok\u00e9mon. (Don't apply Weakness and Resistance.)",
            cost={PokemonTypes.PSYCHIC: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Water Spray",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage; if tails, this attack does 20 damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)