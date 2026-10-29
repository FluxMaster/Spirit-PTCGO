"""STUB: effect not implemented — do not guess mechanics.
Shining Lugia (Promo_SM #SM82): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="716075ec-3ba0-526f-87bd-7a4193e7cd93",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningLugia.Name",
    display_name="Shining Lugia",
    searchable_by=["Shining Lugia", "Basic", "ShiningLugia"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Attack(
            title="Argent Wing",
            game_text="If your opponent's Active Pok\u00e9mon has an Ability, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Aero Force",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)