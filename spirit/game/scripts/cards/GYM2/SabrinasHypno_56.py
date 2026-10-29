"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Hypno (GYM2 #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5c6b47fd-3ace-5ceb-b033-be1b8958bb0b",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasHypno.Name",
    display_name="Sabrina's Hypno",
    searchable_by=["Sabrina's Hypno", "Stage 1", "SabrinasHypno"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasDrowzee.Name",
    family_id=96,
    abilities=[
        Attack(
            title="Invigorate",
            game_text="Choose 1 Basic Pok\u00e9mon in any player's discard pile. Put it onto that player's Bench. Put a number of damage counters on that Pok\u00e9mon equal to half its HP (rounded down to the nearest 10). (You can't put a Pok\u00e9mon on a Bench that's full.)",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Pendulum Curse",
            game_text="Flip a number of coins equal to the number of damage counters on the Defending Pok\u00e9mon. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)