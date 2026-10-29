"""STUB: effect not implemented — do not guess mechanics.
Smeargle (SM8 #157): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="62f853c5-d6d1-550d-b02c-155346035ddc",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic", "Smeargle"],
    subtypes=["Basic"],
    collector_number=157,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Attack(
            title="Stunning Likeness",
            game_text="Your opponent reveals their hand. You may use the effect of a Supporter card you find there as the effect of this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tail Smash",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=flip_or_nothing(),
        ),
    ],
)