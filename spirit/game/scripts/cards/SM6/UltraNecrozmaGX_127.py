"""STUB: effect not implemented — do not guess mechanics.
Ultra Necrozma-GX (SM6 #127): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d76fc849-cef1-591a-9f53-aa843d20eecc",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UltraNecrozmaGX.Name",
    display_name="Ultra Necrozma-GX",
    searchable_by=["Ultra Necrozma-GX", "Basic", "GX", "Ultra Beast", "UltraNecrozmaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=127,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=800,
    abilities=[
        Attack(
            title="Photon Geyser",
            game_text="Discard all basic Psychic Energy from this Pok\u00e9mon. This attack does 80 more damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sky-Scorching Light-GX",
            game_text="You can use this attack only if the total of both players' remaining Prize cards is 6 or less. Put 6 damage counters on each of your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)