"""STUB: effect not implemented — do not guess mechanics.
Ekans (ECARD1 #108): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8c73e356-3b21-58a8-a85d-2573f87df434",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    display_name="Ekans",
    searchable_by=["Ekans", "Basic", "Ekans"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="ECARD1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=23,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)