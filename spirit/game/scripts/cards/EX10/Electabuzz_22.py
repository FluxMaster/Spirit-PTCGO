"""STUB: effect not implemented — do not guess mechanics.
Electabuzz (EX10 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="8cede604-c67d-5566-952a-93b7f145bd8f",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    display_name="Electabuzz",
    searchable_by=["Electabuzz", "Basic", "Electabuzz"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="EX10",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=125,
    abilities=[
        Ability(
            title="Stages of Evolution",
            game_text="As long as Electabuzz is an Evolved Pok\u00e9mon, any damage done to Electabuzz by attacks from your opponent's Pok\u00e9mon that has any Special Energy cards attached to it is reduced by 40 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Double Shock",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads. If either of the coins is heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Luster Blast",
            game_text="Discard 3 Energy attached to Electabuzz.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)