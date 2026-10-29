"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Rattata (GYM1 #82): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="027af8f9-69a5-54da-a91c-69725aa8b5db",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesRattata.Name",
    display_name="Lt. Surge's Rattata",
    searchable_by=["Lt. Surge's Rattata", "Basic", "LtSurgesRattata"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=19,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, Lt. Surge's Rattata's Gnaw attack's base damage is doubled.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)