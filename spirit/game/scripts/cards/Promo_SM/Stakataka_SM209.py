"""STUB: effect not implemented — do not guess mechanics.
Stakataka (Promo_SM #SM209): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="fbadb7b8-3602-5db5-bb44-57001ea3e31d",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stakataka.Name",
    display_name="Stakataka",
    searchable_by=["Stakataka", "Basic", "Ultra Beast", "Stakataka"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=209,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=805,
    abilities=[
        Ability(
            title="Wall of Stone",
            game_text="If your opponent has 3 or fewer Prize cards remaining, this Pok\u00e9mon's maximum HP is 200.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Top Down",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)