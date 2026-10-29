"""STUB: effect not implemented — do not guess mechanics.
Brock's Mankey (GYM1 #67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="1e6bf50d-a440-5dda-abd0-a9466eebc8cc",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksMankey.Name",
    display_name="Brock's Mankey",
    searchable_by=["Brock's Mankey", "Basic", "BrocksMankey"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=56,
    abilities=[
        Attack(
            title="Taunt",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and switch it with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=gust_attack(),
        ),
        Attack(
            title="Light Kick",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)