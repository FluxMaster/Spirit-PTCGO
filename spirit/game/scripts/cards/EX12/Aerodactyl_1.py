"""STUB: effect not implemented — do not guess mechanics.
Aerodactyl (EX12 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="d4d278ae-2bac-5771-aeac-cbbbc8f17d2c",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name",
    display_name="Aerodactyl",
    searchable_by=["Aerodactyl", "Stage 1", "Aerodactyl"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=142,
    abilities=[
        Ability(
            title="Reactive Protection",
            game_text="Any damage done to Aerodactyl by attacks from your opponent's Pok\u00e9mon is reduced by 10 for each React Energy card attached to Aerodactyl (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Power Blow",
            game_text="Does 10 damage plus 10 more damage for each Energy attached to Aerodactyl.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Speed Stroke",
            game_text="During your opponent's next turn, prevent all effects, including damage, done to Aerodactyl by attacks from your opponent's Pok\u00e9mon-ex.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)