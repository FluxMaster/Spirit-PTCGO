"""STUB: effect not implemented — do not guess mechanics.
Trevenant & Dusknoir-GX (Promo_SM #SM217): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8aaf5b56-d8d6-535a-987f-29e9db869b6d",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TrevenantDusknoirGX.Name",
    display_name="Trevenant & Dusknoir-GX",
    searchable_by=["Trevenant & Dusknoir-GX", "Basic", "TAG TEAM", "GX", "TrevenantDusknoirGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=217,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=477,
    abilities=[
        Attack(
            title="Night Watch",
            game_text="Choose 2 random cards from your opponent's hand. Your opponent reveals those cards and shuffles them into their deck.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Pale Moon-GX",
            game_text="At the end of your opponent's next turn, the Defending Pok\u00e9mon will be Knocked Out. If this Pok\u00e9mon has at least 1 extra Psychic Energy attached to it (in addition to this attack's cost), discard all Energy from your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)