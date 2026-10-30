"""STUB: effect not implemented — do not guess mechanics.
Pidgeot (POP2 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="4a0dbed0-168b-50a0-8ee1-b9436f234cb8",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name",
    display_name="Pidgeot",
    searchable_by=["Pidgeot", "Stage 2", "Pidgeot"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="POP2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=18,
    abilities=[
        Ability(
            title="Beating Wings",
            game_text="Once during your turn (before your attack), if Pidgeot is your Active Pok\u00e9mon, you may shuffle 1 of your Benched Pok\u00e9mon and all cards attached to it into your deck. This power can't be used if Pidgeot is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sharp Beak",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)