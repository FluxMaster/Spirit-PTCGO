"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Gastly (GYM1 #93): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="78a91515-482e-5754-8178-06db36376e47",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasGastly.Name",
    display_name="Sabrina's Gastly",
    searchable_by=["Sabrina's Gastly", "Basic", "SabrinasGastly"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Spook",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)