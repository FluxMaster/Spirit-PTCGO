"""STUB: effect not implemented — do not guess mechanics.
Brock's Onix (GYM1 #69): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="7c385a08-68a9-5184-a75c-de7ede472665",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksOnix.Name",
    display_name="Brock's Onix",
    searchable_by=["Brock's Onix", "Basic", "BrocksOnix"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=95,
    abilities=[
        Attack(
            title="Bellow",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)