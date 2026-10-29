"""STUB: effect not implemented — do not guess mechanics.
Mudsdale (Promo_SM #SM20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ce06c856-5998-5c98-bf90-9f9b02114cb7",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudsdale.Name",
    display_name="Mudsdale",
    searchable_by=["Mudsdale", "Stage 1", "Mudsdale"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name",
    family_id=750,
    abilities=[
        Attack(
            title="Enhanced Stomp",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="High Horsepower",
            game_text="This Pok\u00e9mon does 40 damage to itself.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)