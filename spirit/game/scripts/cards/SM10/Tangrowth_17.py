"""STUB: effect not implemented — do not guess mechanics.
Tangrowth (SM10 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ccb72c59-c453-5106-b47f-21538541a313",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name",
    display_name="Tangrowth",
    searchable_by=["Tangrowth", "Stage 1", "Tangrowth"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    family_id=114,
    abilities=[
        Attack(
            title="Bind Down",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Chlorowhip",
            game_text="If this Pok\u00e9mon has at least 2 Grass Energy attached to it, heal 60 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)