"""STUB: effect not implemented — do not guess mechanics.
Buzzwole (HF #SV24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d5706ff6-10bd-5868-8a39-06f790d120ff",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buzzwole.Name",
    display_name="Buzzwole",
    searchable_by=["Buzzwole", "Basic", "Ultra Beast", "Buzzwole"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=93,
    set_code="HF",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=794,
    abilities=[
        Attack(
            title="Sledgehammer",
            game_text="If your opponent has exactly 4 Prize cards remaining, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Swing Around",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)