"""STUB: effect not implemented — do not guess mechanics.
Alolan Sandslash (SM5 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="67c0133f-be9a-5d06-be51-48e52fbcd206",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandslash.Name",
    display_name="Alolan Sandslash",
    searchable_by=["Alolan Sandslash", "Stage 1", "AlolanSandslash"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name",
    family_id=27,
    abilities=[
        Attack(
            title="Spike Armor",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), put 6 damage counters on the Attacking Pok\u00e9mon.",
            cost={},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Frost Breath",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)