"""STUB: effect not implemented — do not guess mechanics.
Espeon & Deoxys-GX (Promo_SM #SM240): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="17056703-bd1a-5bd3-9aca-b3b29e46f2ec",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EspeonDeoxysGX.Name",
    display_name="Espeon & Deoxys-GX",
    searchable_by=["Espeon & Deoxys-GX", "Basic", "TAG TEAM", "GX", "EspeonDeoxysGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=240,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=196,
    abilities=[
        Attack(
            title="Psychic Club",
            game_text="This attack does 30 more damage for each of your Benched Psychic Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cross Division-GX",
            game_text="Put 10 damage counters on your opponent's Pok\u00e9mon in any way you like. If this Pok\u00e9mon has at least 3 extra Energy attached to it (in addition to this attack's cost), put 20 damage counters on them instead. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)