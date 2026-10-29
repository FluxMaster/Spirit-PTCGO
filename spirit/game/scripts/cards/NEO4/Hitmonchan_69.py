"""STUB: effect not implemented — do not guess mechanics.
Hitmonchan (NEO4 #69): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="da0641c4-1b46-5fbd-a271-d348d2d21beb",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name",
    display_name="Hitmonchan",
    searchable_by=["Hitmonchan", "Basic", "Hitmonchan"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=107,
    abilities=[
        Attack(
            title="Dodge",
            game_text="If Hitmonchan would be damaged by an attack during your opponent's next turn, flip a coin. If heads, prevent that attack's damage done to Hitmonchan. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.FIGHTING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Supersonic Jab",
            cost={PokemonTypes.FIGHTING: 3},
            damage=40,
        ),
    ],
)