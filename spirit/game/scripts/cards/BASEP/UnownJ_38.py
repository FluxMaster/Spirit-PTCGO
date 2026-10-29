"""STUB: effect not implemented — do not guess mechanics.
Unown [J] (BASEP #38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="f03b235b-acf4-577c-bd1a-c40df717f790",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownJ.Name",
    display_name="Unown [J]",
    searchable_by=["Unown [J]", "Basic", "UnownJ"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Join]",
            game_text="Once during your turn (before your attack), if you have Unown [J], Unown [O], Unown [I], and Unown Dragon on your Bench, you may search your deck for a Basic Pok\u00e9mon or Evolution card. Show that card to your opponent, then put it into your hand. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)