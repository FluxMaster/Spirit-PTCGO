"""STUB: effect not implemented — do not guess mechanics.
Glameow (SM5 #108): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f1c7981b-864f-521c-ac2e-59ed99c403af",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name",
    display_name="Glameow",
    searchable_by=["Glameow", "Basic", "Glameow"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=431,
    abilities=[
        Attack(
            title="Gentle Bite",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 40 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)