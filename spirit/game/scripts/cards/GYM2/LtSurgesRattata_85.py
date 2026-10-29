"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Rattata (GYM2 #85): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9be7c038-f068-59b0-8aab-111c39be219a",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesRattata.Name",
    display_name="Lt. Surge's Rattata",
    searchable_by=["Lt. Surge's Rattata", "Basic", "LtSurgesRattata"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=19,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, Lt. Surge's Rattata's Quick Attack's base damage is doubled.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)