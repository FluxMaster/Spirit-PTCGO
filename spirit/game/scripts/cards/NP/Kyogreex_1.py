"""STUB: effect not implemented — do not guess mechanics.
Kyogre ex (NP #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b8f84ba8-14ae-5294-bf44-23cd8d55539c",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogreex.Name",
    display_name="Kyogre ex",
    searchable_by=["Kyogre ex", "Basic", "EX", "Kyogreex"],
    subtypes=["Basic", "EX"],
    collector_number=1,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Major Flood",
            game_text="Discard a Water Energy card attached to Kyogre ex. Does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 4},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)