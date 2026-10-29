"""STUB: effect not implemented — do not guess mechanics.
Registeel (Promo_SM #SM75): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f964da9f-b9cc-5e45-b4c0-d50217fd8093",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Registeel.Name",
    display_name="Registeel",
    searchable_by=["Registeel", "Basic", "Registeel"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=379,
    abilities=[
        Attack(
            title="Turbo Arm",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Iron Fist",
            game_text="If Regice is on your Bench, heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)