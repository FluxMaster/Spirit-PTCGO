"""STUB: effect not implemented — do not guess mechanics.
Stunfisk (SM10 #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c144199a-8426-52a9-b940-7fc41a93b7ce",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name",
    display_name="Stunfisk",
    searchable_by=["Stunfisk", "Basic", "Stunfisk"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=618,
    abilities=[
        Attack(
            title="Raging Thunder",
            game_text="This attack does 10 damage to 1 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Electric Trap",
            game_text="This attack does 30 damage for each of your Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)