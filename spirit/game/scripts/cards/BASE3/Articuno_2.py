"""STUB: effect not implemented — do not guess mechanics.
Articuno (BASE3 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="273c99bc-0af1-5351-bdb0-bb5ff6ea4dac",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="BASE3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Attack(
            title="Freeze Dry",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 3},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Blizzard",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. If tails, this attack does 10 damage to each of your own Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 4},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)