"""STUB: effect not implemented — do not guess mechanics.
Yungoos (SM5 #112): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="997e7741-ae6e-57ac-a1cc-bd0902057f6d",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    display_name="Yungoos",
    searchable_by=["Yungoos", "Basic", "Yungoos"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=734,
    abilities=[
        Attack(
            title="Scout",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)