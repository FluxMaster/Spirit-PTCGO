"""STUB: effect not implemented — do not guess mechanics.
Venonat (BASE4 #97): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="276564a1-630a-58e0-a80e-05bd401d916e",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    display_name="Venonat",
    searchable_by=["Venonat", "Basic", "Venonat"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="BASE4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=48,
    abilities=[
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Leech Life",
            game_text="Remove a number of damage counters from Venonat equal to the damage done to the Defending Pok\u00e9mon (after applying Weakness and Resistance). If Venonat has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)