"""STUB: effect not implemented — do not guess mechanics.
Bruxish (Promo_SM #SM11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="92904e58-b88e-50c3-91c2-e94c8565a10c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bruxish.Name",
    display_name="Bruxish",
    searchable_by=["Bruxish", "Basic", "Bruxish"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=779,
    abilities=[
        Attack(
            title="Vivid Charge",
            game_text="Search your deck for up to 3 basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Fang",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)