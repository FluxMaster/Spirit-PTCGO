"""STUB: effect not implemented — do not guess mechanics.
Linoone (TK1B #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="58f7f4a1-d67e-5845-bb6a-43803079e1e3",
    key="TK1B",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Linoone.Name",
    display_name="Linoone",
    searchable_by=["Linoone", "Stage 1", "Linoone"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="TK1B",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Seek Out",
            game_text="Search your deck for up to 2 cards and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Continuous Headbutt",
            game_text="Flip a coin until you get tails. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)