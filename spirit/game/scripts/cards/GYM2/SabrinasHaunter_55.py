"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Haunter (GYM2 #55): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="927b1dbc-81ce-5fa1-aaa6-5da1bb49afef",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasHaunter.Name",
    display_name="Sabrina's Haunter",
    searchable_by=["Sabrina's Haunter", "Stage 1", "SabrinasHaunter"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasGastly.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Nightmare",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Attack",
            game_text="Flip a coin. If heads, and if your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 30 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)