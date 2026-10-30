"""STUB: effect not implemented — do not guess mechanics.
Yanmega (POP8 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9f2c431d-885d-52b3-b497-172a97c38899",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name",
    display_name="Yanmega",
    searchable_by=["Yanmega", "Stage 1", "Yanmega"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="POP8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    family_id=469,
    abilities=[
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Air Slash",
            game_text="Flip a coin. If tails, discard an Energy attached to Yanmega.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)