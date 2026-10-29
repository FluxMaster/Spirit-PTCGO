"""STUB: effect not implemented — do not guess mechanics.
Necrozma (Promo_SM #SM204): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4109f69b-f261-59c8-8bed-2080e190560f",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Necrozma.Name",
    display_name="Necrozma",
    searchable_by=["Necrozma", "Basic", "Necrozma"],
    subtypes=["Basic"],
    collector_number=204,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
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