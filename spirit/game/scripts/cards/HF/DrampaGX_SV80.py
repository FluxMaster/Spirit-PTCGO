"""STUB: effect not implemented — do not guess mechanics.
Drampa-GX (HF #SV80): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="23ea3af9-af92-5b01-836f-e6437ec97fa5",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrampaGX.Name",
    display_name="Drampa-GX",
    searchable_by=["Drampa-GX", "Basic", "GX", "DrampaGX"],
    subtypes=["Basic", "GX"],
    collector_number=149,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=780,
    abilities=[
        Attack(
            title="Righteous Edge",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Berserk",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Big Wheel-GX",
            game_text="Shuffle your hand into your deck. Then, draw 10 cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)