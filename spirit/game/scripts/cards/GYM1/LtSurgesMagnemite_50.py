"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Magnemite (GYM1 #50): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3cb66ba4-70ca-5666-8e03-be11b7c4f2e6",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesMagnemite.Name",
    display_name="Lt. Surge's Magnemite",
    searchable_by=["Lt. Surge's Magnemite", "Basic", "LtSurgesMagnemite"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=81,
    abilities=[
        Attack(
            title="Removal Pulse",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, flip a coin. If heads, choose 1 of those Energy cards and discard it.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Confusion Pulse",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)