"""STUB: effect not implemented — do not guess mechanics.
Alakazam (DP2 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="f6924df9-3e53-5e83-b057-3b944f0afd9a",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alakazam.Name",
    display_name="Alakazam",
    searchable_by=["Alakazam", "Stage 2", "Alakazam"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="DP2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    family_id=65,
    abilities=[
        Ability(
            title="Power Cancel",
            game_text="Once during your opponent's turn, when your opponent's Pok\u00e9mon uses any Pok\u00e9-Power, you may discard 2 cards from your hand and prevent all effects of that Pok\u00e9-Power. (This counts as that Pok\u00e9mon using its Pok\u00e9-Power.) This power can't be used if Alakazam is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Guard",
            game_text="During your opponent's next turn, any damage done to Alakazam by attacks from your opponent's Stage 2 Evolved Pok\u00e9mon is reduced by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)