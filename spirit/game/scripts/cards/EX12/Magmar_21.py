"""STUB: effect not implemented — do not guess mechanics.
Magmar (EX12 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="4156789e-499b-56dd-910c-e2066b23f60b",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic", "Magmar"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="EX12",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Ability(
            title="Stages of Evolution",
            game_text="As long as Magmar is an Evolved Pok\u00e9mon, all Energy attached to Magmar are Fire Energy instead of their usual types.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Linear Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Burning Sensation",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 3},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)