"""STUB: effect not implemented — do not guess mechanics.
Silvally-GX (Promo_SM #SM91): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="d3b3138d-324c-5157-a369-dcbd0ef91c7b",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SilvallyGX.Name",
    display_name="Silvally-GX",
    searchable_by=["Silvally-GX", "Stage 1", "GX", "SilvallyGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=91,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    family_id=773,
    abilities=[
        Ability(
            title="Gyro Unit",
            game_text="Your Basic Pok\u00e9mon in play have no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Turbo Drive",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rebel-GX",
            game_text="This attack does 50 damage for each of your opponent's Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)