"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Haunter (GYM1 #58): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f7790d66-0ef9-5899-8d9d-ef052733d58d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasHaunter.Name",
    display_name="Sabrina's Haunter",
    searchable_by=["Sabrina's Haunter", "Stage 1", "SabrinasHaunter"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasGastly.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Night Spirits",
            game_text="Flip a number of coins equal to the total number of Sabrina's Gastlys, Sabrina's Haunters, and Sabrina's Gengars you have in play. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)