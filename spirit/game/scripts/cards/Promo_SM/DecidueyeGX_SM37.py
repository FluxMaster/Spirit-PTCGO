"""STUB: effect not implemented — do not guess mechanics.
Decidueye-GX (Promo_SM #SM37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="284f3aed-3956-53f4-82e5-62639b50c237",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DecidueyeGX.Name",
    display_name="Decidueye-GX",
    searchable_by=["Decidueye-GX", "Stage 2", "GX", "DecidueyeGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=37,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=724,
    abilities=[
        Ability(
            title="Feather Arrow",
            game_text="Once during your turn (before your attack), you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
        Attack(
            title="Hollow Hunt-GX",
            game_text="Put 3 cards from your discard pile into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)