"""STUB: effect not implemented — do not guess mechanics.
Dark Hypno (BASE5 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37d553de-aae3-5d21-8c70-70ae09d07c07",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkHypno.Name",
    display_name="Dark Hypno",
    searchable_by=["Dark Hypno", "Stage 1", "DarkHypno"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="BASE5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Attack(
            title="Psypunch",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
        Attack(
            title="Bench Manipulation",
            game_text="Your opponent flips a number of coins equal to the number of Pok\u00e9mon on his or her Bench. This attack does 20 damage times the number of tails. Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)