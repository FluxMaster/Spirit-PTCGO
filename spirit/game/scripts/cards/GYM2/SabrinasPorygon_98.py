"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Porygon (GYM2 #98): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dcd3a6ff-b1a4-5c71-bb00-b09579f81098",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasPorygon.Name",
    display_name="Sabrina's Porygon",
    searchable_by=["Sabrina's Porygon", "Basic", "SabrinasPorygon"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=137,
    abilities=[
        Attack(
            title="Sharp Point",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Barrier Attack",
            game_text="All damage done by attacks to Sabrina's Porygon during your opponent's next turn is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)