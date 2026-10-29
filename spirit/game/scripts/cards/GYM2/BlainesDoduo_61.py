"""STUB: effect not implemented — do not guess mechanics.
Blaine's Doduo (GYM2 #61): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="0faca75c-d03f-5ac8-81d7-fa8ed34aed85",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesDoduo.Name",
    display_name="Blaine's Doduo",
    searchable_by=["Blaine's Doduo", "Basic", "BlainesDoduo"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=84,
    abilities=[
        Attack(
            title="Wild Kick",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Retaliate",
            game_text="Does 10 damage times the number of damage counters on Blaine's Doduo.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)