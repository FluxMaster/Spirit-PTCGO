"""STUB: effect not implemented — do not guess mechanics.
Dragonite ex (EX3 #90): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="90cb932b-8903-58cf-9e05-0cbf7892ee1f",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragoniteex.Name",
    display_name="Dragonite ex",
    searchable_by=["Dragonite ex", "Stage 2", "ex", "Dragoniteex"],
    subtypes=["Stage 2", "ex"],
    collector_number=90,
    set_code="EX3",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Call for Power",
            game_text="As often as you like during your turn, you may move an Energy card attached to 1 of your Pok\u00e9mon to Dragonite ex. This power can't be used if Dragonite ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Wave",
            game_text="Discard a Water Energy card and a Lightning Energy card attached to Dragonite ex.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Giant Tail",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            # STUB: attack effect not implemented
            effect=flip_or_nothing(),
        ),
    ],
)