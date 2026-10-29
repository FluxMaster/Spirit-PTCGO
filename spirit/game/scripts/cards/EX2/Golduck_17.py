"""STUB: effect not implemented — do not guess mechanics.
Golduck (EX2 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="b4a7a50b-d20d-552e-b01b-aed4ad941985",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    display_name="Golduck",
    searchable_by=["Golduck", "Stage 1", "Golduck"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="EX2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Ability(
            title="Chaos Flash",
            game_text="Once during your turn (before your attack), if Golduck is your Active Pok\u00e9mon, you may flip a coin. If heads, the Defending Pok\u00e9mon (choose 1 if there are 2) is now Confused. This power can't be used if Golduck is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Special Blow",
            game_text="If the Defending Pok\u00e9mon has any Special Energy cards attached to it, this attack does 30 damage plus 40 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)