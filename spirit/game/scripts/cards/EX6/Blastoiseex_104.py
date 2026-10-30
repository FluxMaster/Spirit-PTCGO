"""STUB: effect not implemented — do not guess mechanics.
Blastoise ex (EX6 #104): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ab5762c1-4383-5b19-9cf7-51782efe1712",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoiseex.Name",
    display_name="Blastoise ex",
    searchable_by=["Blastoise ex", "Stage 2", "ex", "Blastoiseex"],
    subtypes=["Stage 2", "ex"],
    collector_number=104,
    set_code="EX6",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Energy Rain",
            game_text="As often as you like during your turn (before your attack), you may attach a Water Energy card from your hand to 1 of your Pok\u00e9mon. Put 1 damage counter on that Pok\u00e9mon. This power can't be used if Blastoise ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hyper Whirlpool",
            game_text="Flip a coin until you get tails. For each heads, your opponent discards an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)