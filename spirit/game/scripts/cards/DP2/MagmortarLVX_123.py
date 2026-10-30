"""STUB: effect not implemented — do not guess mechanics.
Magmortar LV.X (DP2 #123): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ea5fc6a9-40a8-511a-9344-c1fb60c2d6b7",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagmortarLVX.Name",
    display_name="Magmortar LV.X",
    searchable_by=["Magmortar LV.X", "Level-Up", "MagmortarLVX"],
    subtypes=["Level-Up"],
    collector_number=123,
    set_code="DP2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.LEVELUP,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name",
    family_id=126,
    abilities=[
        Ability(
            title="Torrid Wave",
            game_text="Once during your turn (before your attack), if Magmortar is your Active Pok\u00e9mon, you may choose 1 of the Defending Pok\u00e9mon. That Pok\u00e9mon is now Burned. Put 3 damage counters instead of 2 on that Pok\u00e9mon between turns. This power can't be used if Magmortar is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flame Bluster",
            game_text="Discard 2 Fire Energy attached to Magmortar. Choose 1 of your opponent's Pok\u00e9mon. This attack does 100 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) During your next turn, Magmortar can't use Flame Bluster.",
            cost={PokemonTypes.FIRE: 4},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)