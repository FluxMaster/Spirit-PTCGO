"""STUB: effect not implemented — do not guess mechanics.
Naganadel-GX (Promo_SM #SM125): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="58dec95c-8d58-5041-aa00-e9e1b756e2cf",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NaganadelGX.Name",
    display_name="Naganadel-GX",
    searchable_by=["Naganadel-GX", "Stage 1", "GX", "Ultra Beast", "NaganadelGX"],
    subtypes=["Stage 1", "GX", "Ultra Beast"],
    collector_number=125,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poipole.Name",
    family_id=804,
    abilities=[
        Attack(
            title="Beast Raid",
            game_text="This attack does 20 damage for each of your Ultra Beasts in play.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Jet Needle",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Stinger-GX",
            game_text="Both players shuffle their Prize cards into their decks. Then, each player puts the top 3 cards of their deck face down as their Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)