"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Gastly (GYM2 #96): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="82cc0a32-d2a3-5c65-9026-8361ba19d62e",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasGastly.Name",
    display_name="Sabrina's Gastly",
    searchable_by=["Sabrina's Gastly", "Basic", "SabrinasGastly"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Lick",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fade Out",
            game_text="Return Sabrina's Gastly and all Energy cards attached to it to your hand. (Discard all other cards attached to Sabrina's Gastly.)",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)