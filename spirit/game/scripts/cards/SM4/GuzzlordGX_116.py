"""STUB: effect not implemented — do not guess mechanics.
Guzzlord-GX (SM4 #116): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c968be91-9fc6-5a57-805a-740e910a1abd",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GuzzlordGX.Name",
    display_name="Guzzlord-GX",
    searchable_by=["Guzzlord-GX", "Basic", "GX", "Ultra Beast", "GuzzlordGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=116,
    set_code="SM4",
    rarity=Rarities.RareRainbow,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=799,
    abilities=[
        Attack(
            title="Eat Sloppily",
            game_text="Discard the top 5 cards of your deck. If any of those cards are Energy cards, attach them to this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tyrannical Hole",
            cost={PokemonTypes.DARKNESS: 3, PokemonTypes.COLORLESS: 2},
            damage=180,
        ),
        Attack(
            title="Glutton-GX",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from this attack, take 2 more Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 5},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)