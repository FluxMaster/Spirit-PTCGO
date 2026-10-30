"""STUB: effect not implemented — do not guess mechanics.
Mew ex (EX12 #88): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="377af9b1-d687-5b96-bc24-4eef79044b0f",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewex.Name",
    display_name="Mew ex",
    searchable_by=["Mew ex", "Basic", "ex", "Mewex"],
    subtypes=["Basic", "ex"],
    collector_number=88,
    set_code="EX12",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Versatile",
            game_text="Mew ex can use the attacks of all Pok\u00e9mon in play as its own. (You still need the necessary Energy to use each attack.)",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Power Move",
            game_text="Search your deck for an Energy card and attach it to Mew ex. Shuffle your deck afterward. Then, you may switch Mew ex with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)