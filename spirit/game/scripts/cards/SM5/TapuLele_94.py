"""STUB: effect not implemented — do not guess mechanics.
Tapu Lele (SM5 #94): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6619d4c4-c003-5621-94af-589af3744202",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuLele.Name",
    display_name="Tapu Lele",
    searchable_by=["Tapu Lele", "Basic", "TapuLele"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=786,
    abilities=[
        Attack(
            title="Psywave",
            game_text="This attack does 20 damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Magical Swap",
            game_text="Move any number of damage counters on your opponent's Pok\u00e9mon to their other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)