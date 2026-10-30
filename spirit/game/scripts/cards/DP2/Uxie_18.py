"""STUB: effect not implemented — do not guess mechanics.
Uxie (DP2 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="a03f6da9-fb05-5d36-aabb-3e98a005439c",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name",
    display_name="Uxie",
    searchable_by=["Uxie", "Basic", "Uxie"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="DP2",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=480,
    abilities=[
        Ability(
            title="Memory Out",
            game_text="Once during your opponent's turn, if Uxie is damaged by an opponent's attack (even if Uxie is Knocked Out), you may use this power. The Attacking Pok\u00e9mon can't use that attack during your opponent's next turn.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mind Off",
            game_text="If you have Mesprit and Azelf in play, this attack does 10 damage plus 20 more damage and the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)