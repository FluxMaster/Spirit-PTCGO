"""STUB: effect not implemented — do not guess mechanics.
Regice ex (EX5 #97): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="36974ebc-b7ba-5c7c-9a0f-e65bcfe5f78d",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regiceex.Name",
    display_name="Regice ex",
    searchable_by=["Regice ex", "Basic", "ex", "Regiceex"],
    subtypes=["Basic", "ex"],
    collector_number=97,
    set_code="EX5",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=378,
    abilities=[
        Ability(
            title="Crystal Body",
            game_text="Prevent all effects of attacks, except damage, done to Regice ex by the Attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Freeze Lock",
            game_text="Flip a coin. If heads, your opponent can't attach Energy cards from his or her hand to the Defending Pok\u00e9mon during his or her next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)