"""STUB: effect not implemented — do not guess mechanics.
Blaine's Rhyhorn (GYM2 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="60f34e63-4c21-5572-906a-ead35d7c2319",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesRhyhorn.Name",
    display_name="Blaine's Rhyhorn",
    searchable_by=["Blaine's Rhyhorn", "Basic", "BlainesRhyhorn"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=111,
    abilities=[
        Attack(
            title="Horn Charge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Overrun",
            game_text="Flip a coin. If heads and if your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 20 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)