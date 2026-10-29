"""STUB: effect not implemented — do not guess mechanics.
Necrozma (SM11 #101): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0b888e01-f61b-59e7-9b2d-773ab2161213",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Necrozma.Name",
    display_name="Necrozma",
    searchable_by=["Necrozma", "Basic", "Necrozma"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=800,
    abilities=[
        Attack(
            title="Barrier Attack",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Special Laser",
            game_text="If this Pok\u00e9mon has any Special Energy attached to it, this attack does 60 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)