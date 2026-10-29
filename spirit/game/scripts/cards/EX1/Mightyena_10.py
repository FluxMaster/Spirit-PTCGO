"""STUB: effect not implemented — do not guess mechanics.
Mightyena (EX1 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="3c69eb9c-c811-517f-b526-66e0971f3efa",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name",
    display_name="Mightyena",
    searchable_by=["Mightyena", "Stage 1", "Mightyena"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    family_id=261,
    abilities=[
        Ability(
            title="Intimidating Fang",
            game_text="As long as Mightyena is your Active Pok\u00e9mon, any damage done to your Pok\u00e9mon by an opponent's attack is reduced by 10 (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shakedown",
            game_text="Flip a coin. If heads, choose 1 card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)