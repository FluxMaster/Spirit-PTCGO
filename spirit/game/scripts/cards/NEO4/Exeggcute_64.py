"""STUB: effect not implemented — do not guess mechanics.
Exeggcute (NEO4 #64): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="b47a6794-e4ac-5bae-98a9-749e25a3e57c",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    display_name="Exeggcute",
    searchable_by=["Exeggcute", "Basic", "Exeggcute"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=102,
    abilities=[
        Attack(
            title="Sleep Powder",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Psyshock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)