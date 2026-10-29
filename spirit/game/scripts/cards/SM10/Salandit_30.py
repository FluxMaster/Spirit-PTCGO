"""STUB: effect not implemented — do not guess mechanics.
Salandit (SM10 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0cd6a391-3dec-5fa7-b860-db146ab05157",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    display_name="Salandit",
    searchable_by=["Salandit", "Basic", "Salandit"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=757,
    abilities=[
        Attack(
            title="Grass Fire",
            game_text="Discard a Grass Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)