"""STUB: effect not implemented — do not guess mechanics.
Lunala-GX (SM5 #172): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2e7dbc75-9cbd-593d-b3a9-d74f806ce288",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LunalaGX.Name",
    display_name="Lunala-GX",
    searchable_by=["Lunala-GX", "Stage 2", "GX", "LunalaGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=172,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=789,
    abilities=[
        Ability(
            title="Psychic Transfer",
            game_text="As often as you like during your turn (before your attack), you may move a Psychic Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Moongeist Beam",
            game_text="The Defending Pok\u00e9mon can't be healed during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 4},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lunar Fall-GX",
            game_text="Knock Out 1 of your opponent's Basic Pok\u00e9mon that isn't a Pok\u00e9mon-GX. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)