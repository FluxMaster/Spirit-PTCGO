"""STUB: effect not implemented — do not guess mechanics.
Wishiwashi (SM2 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="e99b05f9-ce13-5ac0-94ff-1bb89ea4e402",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name",
    display_name="Wishiwashi",
    searchable_by=["Wishiwashi", "Basic", "Wishiwashi"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Ability(
            title="Schooling",
            game_text="Once during your turn (before your attack), you may switch this Pok\u00e9mon with a Wishiwashi-GX in your hand. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sharpshooting",
            game_text="This attack does 10 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=snipe_attack(10, pool='any', count=1),
        ),
    ],
)