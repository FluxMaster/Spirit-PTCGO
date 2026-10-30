"""STUB: effect not implemented — do not guess mechanics.
Spheal (DP2 #102): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="05d97fd5-976f-5f7d-84e1-122a4597bab2",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name",
    display_name="Spheal",
    searchable_by=["Spheal", "Basic", "Spheal"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="DP2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=363,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Willpower",
            game_text="Flip a coin. If heads, during your next turn, Spheal's Rollout attack's base damage is 40.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)