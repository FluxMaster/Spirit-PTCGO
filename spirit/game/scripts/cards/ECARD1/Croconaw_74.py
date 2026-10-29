"""STUB: effect not implemented — do not guess mechanics.
Croconaw (ECARD1 #74): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b3c978d4-b708-577b-90e4-8e16b69e856d",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    display_name="Croconaw",
    searchable_by=["Croconaw", "Stage 1", "Croconaw"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    family_id=158,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Take Down",
            game_text="Croconaw does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)