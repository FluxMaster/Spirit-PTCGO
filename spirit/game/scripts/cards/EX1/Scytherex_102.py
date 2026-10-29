"""STUB: effect not implemented — do not guess mechanics.
Scyther ex (EX1 #102): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="32b6b8d0-3d90-5533-8c55-95a40ffa399e",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scytherex.Name",
    display_name="Scyther ex",
    searchable_by=["Scyther ex", "Basic", "ex", "Scytherex"],
    subtypes=["Basic", "ex"],
    collector_number=102,
    set_code="EX1",
    rarity=Rarities.RareHoloEX,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=123,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Scyther ex during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)