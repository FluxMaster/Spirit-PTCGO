"""STUB: effect not implemented — do not guess mechanics.
Swampert ex (EX14 #98): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="16713b9f-f1ef-528b-9a86-e15b5c7733e0",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swampertex.Name",
    display_name="Swampert ex",
    searchable_by=["Swampert ex", "Stage 2", "ex", "Swampertex"],
    subtypes=["Stage 2", "ex"],
    collector_number=98,
    set_code="EX14",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    family_id=258,
    abilities=[
        Ability(
            title="Energy Recycle",
            game_text="Once during your turn (before your attack), you may search your discard pile for 3 Energy cards and attach them to your Pok\u00e9mon in any way you like. If you do, your turn ends. This power can't be used if Swampert ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ultra Pump",
            game_text="You may discard 2 cards from your hand. If you do, this attack does 60 damage plus 20 more damage and does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)