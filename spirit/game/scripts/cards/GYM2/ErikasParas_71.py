"""STUB: effect not implemented — do not guess mechanics.
Erika's Paras (GYM2 #71): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="01bc1c3f-6d35-53d1-8c46-566c0ad3ac7c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasParas.Name",
    display_name="Erika's Paras",
    searchable_by=["Erika's Paras", "Basic", "ErikasParas"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=46,
    abilities=[
        Attack(
            title="Irongrip",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Poison Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned and this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)