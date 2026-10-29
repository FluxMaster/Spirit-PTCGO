"""STUB: effect not implemented — do not guess mechanics.
Weavile-GX (SM11 #132): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="95d0a59a-9cb3-5032-beeb-a405170a7ca6",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WeavileGX.Name",
    display_name="Weavile-GX",
    searchable_by=["Weavile-GX", "Stage 1", "GX", "WeavileGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=132,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Ability(
            title="Shadow Connection",
            game_text="As often as you like during your turn (before your attack), you may move a basic Darkness Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Nocturnal Maneuvers-GX",
            game_text="Search your deck for any number of Basic Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)