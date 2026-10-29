"""STUB: effect not implemented — do not guess mechanics.
Bewear (Promo_SM #SM49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="21aba8e7-07ca-52df-b041-0991ef37309d",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1", "Bewear"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=760,
    abilities=[
        Attack(
            title="Mix-Up",
            game_text="Flip a coin. If heads, discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tantrum",
            game_text="This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)