"""STUB: effect not implemented — do not guess mechanics.
Lanturn (EX5 #38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2d914620-6f15-5602-884f-d6c83f113e38",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1", "Lanturn"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Ability(
            title="Energy Grounding",
            game_text="Once during your opponent's turn, when any of your Pok\u00e9mon is Knocked Out by your opponent's attacks, you may use this power. Choose a basic Energy card discarded from the Knocked Out Pok\u00e9mon and attach it to Lanturn. You can't use more than 1 Energy Grounding Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lightning Strike",
            game_text="You may discard all Lightning Energy attached to Lanturn. If you do, this attack's base damage is 90 instead of 50.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)