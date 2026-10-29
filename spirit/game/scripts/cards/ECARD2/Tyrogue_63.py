"""STUB: effect not implemented — do not guess mechanics.
Tyrogue (ECARD2 #63): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca352581-af62-5bd2-96ac-46e534f66ecf",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrogue.Name",
    display_name="Tyrogue",
    searchable_by=["Tyrogue", "Baby", "Tyrogue"],
    subtypes=["Baby"],
    collector_number=63,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=236,
    abilities=[
        Attack(
            title="Energy Punch",
            game_text="Flip a coin. If heads, discard a Special Energy card attached to the Defending Pok\u00e9mon. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)