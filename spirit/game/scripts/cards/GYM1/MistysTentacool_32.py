"""STUB: effect not implemented — do not guess mechanics.
Misty's Tentacool (GYM1 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="6fddd794-102c-5d59-8508-ae1ead79833b",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysTentacool.Name",
    display_name="Misty's Tentacool",
    searchable_by=["Misty's Tentacool", "Basic", "MistysTentacool"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=72,
    abilities=[
        Attack(
            title="Mysterious Light",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
        Attack(
            title="Jellyfish Pod",
            game_text="Search your deck for any number of Pok\u00e9mon named Tentacool, Tentacruel, Misty's Tentacool, and/or Misty's Tentacruel. Show those cards to your opponent, then put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)