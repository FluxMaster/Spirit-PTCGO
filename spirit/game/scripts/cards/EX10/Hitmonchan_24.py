"""STUB: effect not implemented — do not guess mechanics.
Hitmonchan (EX10 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="e3a06de7-a1c0-5bcf-9f89-ba88af73e4e5",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name",
    display_name="Hitmonchan",
    searchable_by=["Hitmonchan", "Basic", "Hitmonchan"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="EX10",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=107,
    abilities=[
        Ability(
            title="Stages of Evolution",
            game_text="As long as Hitmonchan is an Evolved Pok\u00e9mon, Hitmonchan gets +30 HP.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Punch",
            game_text="Does 10 damage times the number of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Speedy Uppercut",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)