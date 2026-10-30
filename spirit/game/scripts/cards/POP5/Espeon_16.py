"""STUB: effect not implemented — do not guess mechanics.
Espeon ★ (POP5 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="acd30c7d-b060-5081-81ad-cc053b03bd59",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon ★",
    searchable_by=["Espeon \u2605", "Basic", "Star", "Espeon"],
    subtypes=["Basic", "Star"],
    collector_number=16,
    set_code="POP5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=196,
    abilities=[
        Ability(
            title="Purple Ray",
            game_text="Once during your turn, when you put Espeon Star from your hand onto your Bench, you may use this power. Each Active Pok\u00e9mon (both yours and your opponent's) is now Confused.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Boom",
            game_text="Does 30 damage plus 10 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)