"""STUB: effect not implemented — do not guess mechanics.
Magmar (SM11 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm8 import smokescreen


card = PokemonCardDef(
    guid="32d157c2-d002-5ad9-8697-f2491c2d977d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic", "Magmar"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Attack(
            title="Smoke Bomb",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=smokescreen,
        ),
    ],
)