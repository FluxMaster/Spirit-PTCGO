"""STUB: effect not implemented — do not guess mechanics.
Misty's Horsea (GYM2 #87): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="078b1ec3-58f9-5c41-9cb2-4aa629971728",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysHorsea.Name",
    display_name="Misty's Horsea",
    searchable_by=["Misty's Horsea", "Basic", "MistysHorsea"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=116,
    abilities=[
        Attack(
            title="Ink Spurt",
            game_text="Flip a coin. If heads, whenever the Defending Pok\u00e9mon tries to attack, your opponent flips a coin. If tails, that attack does nothing. (This effect lasts until the Defending Pok\u00e9mon evolves or is Benched.)",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)