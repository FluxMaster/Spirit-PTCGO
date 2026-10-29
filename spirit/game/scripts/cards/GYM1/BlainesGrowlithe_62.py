"""STUB: effect not implemented — do not guess mechanics.
Blaine's Growlithe (GYM1 #62): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f5ae1810-6515-5b0f-a59f-416b9e5cbb7d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesGrowlithe.Name",
    display_name="Blaine's Growlithe",
    searchable_by=["Blaine's Growlithe", "Basic", "BlainesGrowlithe"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Blaze",
            game_text="Does 10 damage to each Grass Pok\u00e9mon on your opponent's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)