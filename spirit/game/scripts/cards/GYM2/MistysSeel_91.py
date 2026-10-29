"""STUB: effect not implemented — do not guess mechanics.
Misty's Seel (GYM2 #91): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, smokescreen_attack


card = PokemonCardDef(
    guid="e6e3ced6-db3c-5d03-bbd6-c6020a9eaf71",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysSeel.Name",
    display_name="Misty's Seel",
    searchable_by=["Misty's Seel", "Basic", "MistysSeel"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=86,
    abilities=[
        Attack(
            title="Frostbite",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Mirage",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=smokescreen_attack(),
        ),
    ],
)