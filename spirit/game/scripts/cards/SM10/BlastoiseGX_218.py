"""STUB: effect not implemented — do not guess mechanics.
Blastoise-GX (SM10 #218): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import takes_less_passive


card = PokemonCardDef(
    guid="1b2a7172-ce31-5e06-9930-336dc06277f3",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseGX.Name",
    display_name="Blastoise-GX",
    searchable_by=["Blastoise-GX", "Stage 2", "GX", "BlastoiseGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=218,
    set_code="SM10",
    rarity=Rarities.RareRainbow,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Solid Shell",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Rocket Splash",
            game_text="Shuffle any amount of Water Energy from your Pok\u00e9mon into your deck. This attack does 60 damage for each card you shuffled into your deck in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Giant Geyser-GX",
            game_text="Attach any number of Water Energy cards from your hand to your Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)