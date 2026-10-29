"""STUB: effect not implemented — do not guess mechanics.
Cradily (EX2 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="f59ad480-1609-5bad-beb1-4d73a2e302b8",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cradily.Name",
    display_name="Cradily",
    searchable_by=["Cradily", "Stage 2", "Cradily"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    family_id=345,
    abilities=[
        Ability(
            title="Super Suction Cups",
            game_text="As long as Cradily is your Active Pok\u00e9mon, your opponent's Pok\u00e9mon can't retreat.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lure Poison",
            game_text="Before using this effect, you may switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon, if any. The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Spiral Drain",
            game_text="Remove 2 damage counters from Cradily (remove 1 if there is only 1).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)