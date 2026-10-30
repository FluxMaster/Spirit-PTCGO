"""STUB: effect not implemented — do not guess mechanics.
Manaphy (POP9 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="869e9abf-2bda-5596-868b-5f29ed0b1797",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="POP9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Attack(
            title="Dive",
            game_text="Look at the top 7 cards of your deck, choose 1 of them, and put it into your hand. Put the other cards back on top of your deck. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Water Glow",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Remove from Manaphy the number of damage counters equal to the damage you did to that Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)