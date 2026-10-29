"""STUB: effect not implemented — do not guess mechanics.
Banette (SM7 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="806173f5-2c57-5b87-bff8-c5b94ebca9d3",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette", "Stage 1", "Banette"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Ability(
            title="Red Eyes",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put a Basic Pok\u00e9mon from your opponent's discard pile onto their Bench.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Enemy Show",
            game_text="For each of your opponent's Pok\u00e9mon in play, put 1 damage counter on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)