"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Raticate (GYM2 #53): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a03c363-4ade-5913-b1a8-478419846516",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesRaticate.Name",
    display_name="Lt. Surge's Raticate",
    searchable_by=["Lt. Surge's Raticate", "Stage 1", "LtSurgesRaticate"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesRattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, Lt. Surge's Raticate's Double-edge attack's damage (base damage and damage to itself) is doubled.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Double-edge",
            game_text="Lt. Surge's Raticate does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)