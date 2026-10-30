"""STUB: effect not implemented — do not guess mechanics.
Venusaur ex (EX6 #112): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ebcc0e10-9835-515c-8bb4-1e97c9b3e98e",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaurex.Name",
    display_name="Venusaur ex",
    searchable_by=["Venusaur ex", "Stage 2", "ex", "Venusaurex"],
    subtypes=["Stage 2", "ex"],
    collector_number=112,
    set_code="EX6",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Energy Trans",
            game_text="As often as you like during your turn (before your attack), move a Grass Energy card attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Venusaur ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Pollen Hazard",
            game_text="The Defending Pok\u00e9mon is now Poisoned, Burned, and Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)