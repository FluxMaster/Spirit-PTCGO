"""STUB: effect not implemented — do not guess mechanics.
Charizard-GX (Promo_SM #SM195): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm4 import dread_storm_gx


card = PokemonCardDef(
    guid="503aba75-0ade-54b6-a582-12e9015d4b76",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardGX.Name",
    display_name="Charizard-GX",
    searchable_by=["Charizard-GX", "Stage 2", "GX", "CharizardGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=195,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Raging Destruction",
            game_text="Discard the top 8 cards of your deck. If any of those cards are Fire Energy cards, attach them to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Steam Artillery",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 3},
            damage=200,
        ),
        Attack(
            title="Dreadful Flames-GX",
            game_text="Discard an Energy from each of your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 3},
            damage=250,
            # STUB: attack effect not implemented
            effect=dread_storm_gx,
        ),
    ],
)