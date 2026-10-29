"""STUB: effect not implemented — do not guess mechanics.
Tapu Koko-GX (Promo_SM #SM33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="5a71c913-1447-5333-9c65-1fac4dbf6e78",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoGX.Name",
    display_name="Tapu Koko-GX",
    searchable_by=["Tapu Koko-GX", "Basic", "GX", "TapuKokoGX"],
    subtypes=["Basic", "GX"],
    collector_number=33,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=785,
    abilities=[
        Ability(
            title="Aero Trail",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may move any number of Lightning Energy from your other Pok\u00e9mon to this Pok\u00e9mon. If you do, switch this Pok\u00e9mon with your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sky-High Claws",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Tapu Thunder-GX",
            game_text="This attack does 50 damage times the amount of Energy attached to all of your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)