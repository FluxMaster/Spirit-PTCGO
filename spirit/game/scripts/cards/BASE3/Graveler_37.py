"""STUB: effect not implemented — do not guess mechanics.
Graveler (BASE3 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="562380f1-54a8-5c5b-9516-da5e2c13f8c6",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    display_name="Graveler",
    searchable_by=["Graveler", "Stage 1", "Graveler"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, whenever 30 or less damage is done to Graveler (after applying Weakness and Resistance), prevent that damage. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.FIGHTING: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)