"""STUB: effect not implemented — do not guess mechanics.
Luvdisc (POP2 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="097a8656-d562-5182-9983-2bd38f4bd8f5",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name",
    display_name="Luvdisc",
    searchable_by=["Luvdisc", "Basic", "Luvdisc"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="POP2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=370,
    abilities=[
        Attack(
            title="Paralyzing Kiss",
            game_text="If there are 2 Defending Pok\u00e9mon in play, choose 1 of the Defending Pok\u00e9mon. That Pok\u00e9mon is now Paralyzed. (If there is only 1 Defending Pok\u00e9mon, this attack does nothing.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fast Stream",
            game_text="Move 1 Energy card attached to the Defending Pok\u00e9mon to the other Defending Pok\u00e9mon. (Ignore this effect if your opponent has only 1 Defending Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)