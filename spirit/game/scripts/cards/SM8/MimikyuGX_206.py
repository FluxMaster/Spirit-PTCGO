"""STUB: effect not implemented — do not guess mechanics.
Mimikyu-GX (SM8 #206): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="91181f04-2699-5c19-ae99-52091cfc17d6",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MimikyuGX.Name",
    display_name="Mimikyu-GX",
    searchable_by=["Mimikyu-GX", "Basic", "GX", "MimikyuGX"],
    subtypes=["Basic", "GX"],
    collector_number=206,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=778,
    abilities=[
        Attack(
            title="Perplex",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FAIRY: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Let's Snuggle & Fall",
            game_text="This attack does 30 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dream Fear-GX",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. Your opponent shuffles that Pok\u00e9mon and all cards attached to it into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)