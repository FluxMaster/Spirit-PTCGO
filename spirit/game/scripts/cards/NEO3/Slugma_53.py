"""STUB: effect not implemented — do not guess mechanics.
Slugma (NEO3 #53): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="1277409a-b803-5f85-9f60-0801c2884681",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    display_name="Slugma",
    searchable_by=["Slugma", "Basic", "Slugma"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Magma Ring",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(no_retreat=True),
        ),
    ],
)