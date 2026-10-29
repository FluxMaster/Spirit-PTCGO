"""STUB: effect not implemented — do not guess mechanics.
Cubone (SM10 #90): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cd95008b-2d6e-54ee-92e2-f612b7df9181",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    display_name="Cubone",
    searchable_by=["Cubone", "Basic", "Cubone"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=104,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, this Pok\u00e9mon's Beat attack's base damage is 80.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Beat",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)