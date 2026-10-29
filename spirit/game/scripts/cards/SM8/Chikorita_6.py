"""STUB: effect not implemented — do not guess mechanics.
Chikorita (SM8 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="d1edb5e7-9d3b-5247-934a-ee319b3de706",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name",
    display_name="Chikorita",
    searchable_by=["Chikorita", "Basic", "Chikorita"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=152,
    abilities=[
        Attack(
            title="Mini Drain",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=heal_attack(10),
        ),
    ],
)