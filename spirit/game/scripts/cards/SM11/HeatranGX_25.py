"""STUB: effect not implemented — do not guess mechanics.
Heatran-GX (SM11 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="3ae53ab7-1745-5fee-8ecb-ca27cdc1c348",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatranGX.Name",
    display_name="Heatran-GX",
    searchable_by=["Heatran-GX", "Basic", "GX", "HeatranGX"],
    subtypes=["Basic", "GX"],
    collector_number=25,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=485,
    abilities=[
        Ability(
            title="Burning Road",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to become your Active Pok\u00e9mon, you may move any number of Fire Energy from your other Pok\u00e9mon to it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Steaming Stomp",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Hot Burn-GX",
            game_text="This attack does 50 damage times the amount of Fire Energy attached to this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)