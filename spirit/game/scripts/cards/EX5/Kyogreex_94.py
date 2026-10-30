"""STUB: effect not implemented — do not guess mechanics.
Kyogre ex (EX5 #94): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="b03f6be4-16c2-5fdc-b646-7de0d7e46c0e",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogreex.Name",
    display_name="Kyogre ex",
    searchable_by=["Kyogre ex", "Basic", "ex", "Kyogreex"],
    subtypes=["Basic", "ex"],
    collector_number=94,
    set_code="EX5",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=382,
    abilities=[
        Ability(
            title="Mark of Antiquity",
            game_text="As long as Kyogre ex is your Active Pok\u00e9mon, each player's Groudon ex and Rayquaza ex can't attack.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Water Arrow",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Super Tidal Wave",
            game_text="You may show your hand to your opponent. If you do, this attack does 50 damage plus 10 more damage for each Energy card in your hand. After doing damage, shuffle the Energy cards back into your deck.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)