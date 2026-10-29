"""STUB: effect not implemented — do not guess mechanics.
Dark Raichu (BASE6 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9d7e92a1-f4cb-55bd-ac84-0abde0139f40",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkRaichu.Name",
    display_name="Dark Raichu",
    searchable_by=["Dark Raichu", "Stage 1", "DarkRaichu"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="BASE6",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Surprise Thunder",
            game_text="Flip a coin. If heads, flip another coin. If the second coins is heads, this attack does 20 damage to each of your opponent's Benched Pok\u00e9mon. If the second coin is tails, this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)