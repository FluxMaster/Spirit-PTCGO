"""STUB: effect not implemented — do not guess mechanics.
Erika's Bellsprout (GYM1 #75): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="653069ec-f953-5d79-be90-22ff8bdad486",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasBellsprout.Name",
    display_name="Erika's Bellsprout",
    searchable_by=["Erika's Bellsprout", "Basic", "ErikasBellsprout"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=69,
    abilities=[
        Attack(
            title="Poison Vine",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
        ),
    ],
)