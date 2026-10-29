"""STUB: effect not implemented — do not guess mechanics.
Spinarak (SM7 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e26c5e9d-1d85-5d45-88c9-a282639ffb11",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    display_name="Spinarak",
    searchable_by=["Spinarak", "Basic", "Spinarak"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=167,
    abilities=[
        Attack(
            title="Stun Poison",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)