"""STUB: effect not implemented — do not guess mechanics.
Bellsprout (BASE4 #66): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="308adc86-9236-5db6-b397-2d707a0fc4a9",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    display_name="Bellsprout",
    searchable_by=["Bellsprout", "Basic", "Bellsprout"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="BASE4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=69,
    abilities=[
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon named Bellsprout and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)