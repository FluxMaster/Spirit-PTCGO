"""STUB: effect not implemented — do not guess mechanics.
Latias & Latios-GX (SM9 #169): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="132cb4e4-79ce-5a85-a551-6d9b68895812",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiasLatiosGX.Name",
    display_name="Latias & Latios-GX",
    searchable_by=["Latias & Latios-GX", "Basic", "TAG TEAM", "GX", "LatiasLatiosGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=169,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=380,
    abilities=[
        Attack(
            title="Buster Purge",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Aero Unit-GX",
            game_text="Attach 5 basic Energy cards from your discard pile to your Pok\u00e9mon in any way you like. If this Pok\u00e9mon has at least 1 extra Energy attached to it (in addition to this attack's cost), prevent all effects of attacks, including damage, done to it during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)