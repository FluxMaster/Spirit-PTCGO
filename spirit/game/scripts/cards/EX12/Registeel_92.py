"""STUB: effect not implemented — do not guess mechanics.
Registeel ★ (EX12 #92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bcb19410-d2f6-5e34-92a2-a71678175d4e",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Registeel.Name",
    display_name="Registeel ★",
    searchable_by=["Registeel \u2605", "Basic", "Star", "Registeel"],
    subtypes=["Basic", "Star"],
    collector_number=92,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=379,
    abilities=[
        Attack(
            title="Barrier Attack",
            game_text="During your opponent's next turn, any damage done to Registeel Star by attacks is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Final Laser",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like. If your opponent has only 1 Prize card left and Registeel Star is the only Pok\u00e9mon you have in play, put 6 damage counters instead.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)