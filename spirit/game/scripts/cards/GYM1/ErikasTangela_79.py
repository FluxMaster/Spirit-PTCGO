"""STUB: effect not implemented — do not guess mechanics.
Erika's Tangela (GYM1 #79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="e20a22f6-0d66-5d5c-9a3b-3edd175b760f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasTangela.Name",
    display_name="Erika's Tangela",
    searchable_by=["Erika's Tangela", "Basic", "ErikasTangela"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=114,
    abilities=[
        Attack(
            title="Vine Slap",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Stretch Vine",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 20 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=snipe_attack(20),
        ),
    ],
)