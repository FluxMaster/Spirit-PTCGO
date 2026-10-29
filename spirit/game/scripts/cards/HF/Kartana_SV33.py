"""STUB: effect not implemented — do not guess mechanics.
Kartana (HF #SV33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ee10c83a-5f4a-50c0-a8a6-b7ea63146a0a",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kartana.Name",
    display_name="Kartana",
    searchable_by=["Kartana", "Basic", "Ultra Beast", "Kartana"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=102,
    set_code="HF",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=798,
    abilities=[
        Attack(
            title="Divine Paper",
            game_text="If your opponent has exactly 6 Prize cards remaining, this attack does 90 more damage.",
            cost={PokemonTypes.METAL: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)