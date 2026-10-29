"""STUB: effect not implemented — do not guess mechanics.
Flygon-GX (SM12 #256): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.gum import security_guard_passive
from spirit.game.card_effects.attacks_common import ignore_effects_attack


card = PokemonCardDef(
    guid="dd6ae83c-17d8-5a4b-b3b9-1dc5ca9fb233",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlygonGX.Name",
    display_name="Flygon-GX",
    searchable_by=["Flygon-GX", "Stage 2", "GX", "FlygonGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=256,
    set_code="SM12",
    rarity=Rarities.RareRainbow,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Dusty Defense",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, all of your Pok\u00e9mon take 30 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            passive=security_guard_passive,
        ),
        Attack(
            title="Desert Hurricane",
            game_text="If there is any Stadium card in play, this attack does 120 more damage. Then, discard that Stadium card.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=120,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sonic Edge-GX",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 3},
            damage=220,
            # STUB: attack effect not implemented
            effect=ignore_effects_attack(),
        ),
    ],
)