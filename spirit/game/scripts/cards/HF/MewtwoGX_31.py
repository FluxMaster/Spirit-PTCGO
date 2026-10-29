"""STUB: effect not implemented — do not guess mechanics.
Mewtwo-GX (HF #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb5451c2-a51a-553f-b365-5f847e3595f1",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoGX.Name",
    display_name="Mewtwo-GX",
    searchable_by=["Mewtwo-GX", "Basic", "GX", "MewtwoGX"],
    subtypes=["Basic", "GX"],
    collector_number=31,
    set_code="HF",
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
        Attack(
            title="Psycrush-GX",
            game_text="Discard all Energy from your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)