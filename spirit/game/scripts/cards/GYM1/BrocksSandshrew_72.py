"""STUB: effect not implemented — do not guess mechanics.
Brock's Sandshrew (GYM1 #72): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="76817534-6ec6-5d0e-88e3-4f4708779098",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksSandshrew.Name",
    display_name="Brock's Sandshrew",
    searchable_by=["Brock's Sandshrew", "Basic", "BrocksSandshrew"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=27,
    abilities=[
        Attack(
            title="Sand Pit",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)