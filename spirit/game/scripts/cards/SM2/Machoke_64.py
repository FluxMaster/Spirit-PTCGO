"""STUB: effect not implemented — do not guess mechanics.
Machoke (SM2 #64): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="bccb0b1b-2f13-530b-b07b-3fbbf6d17fb5",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    display_name="Machoke",
    searchable_by=["Machoke", "Stage 1", "Machoke"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Daunting Pose",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by your opponent's attacks. Your opponent's attacks and Abilities can't put damage counters on your Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cross Chop",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(30),
        ),
    ],
)