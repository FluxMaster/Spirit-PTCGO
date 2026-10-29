"""STUB: effect not implemented — do not guess mechanics.
Venonat (SM10 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f8f6723e-ffc5-5857-9122-e4587a460e38",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    display_name="Venonat",
    searchable_by=["Venonat", "Basic", "Venonat"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=48,
    abilities=[
        Attack(
            title="Radar Eyes",
            game_text="Look at the top 7 cards of your deck and put 1 of them into your hand. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)