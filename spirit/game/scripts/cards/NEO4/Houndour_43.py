"""STUB: effect not implemented — do not guess mechanics.
Houndour (NEO4 #43): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, flip_or_nothing


card = PokemonCardDef(
    guid="1529f0be-9a7a-5f19-805d-e7b1b8329f3e",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    display_name="Houndour",
    searchable_by=["Houndour", "Basic", "Houndour"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=228,
    abilities=[
        Attack(
            title="Corner",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Lunge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=flip_or_nothing(),
        ),
    ],
)