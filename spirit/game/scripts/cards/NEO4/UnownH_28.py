"""STUB: effect not implemented — do not guess mechanics.
Unown [H] (NEO4 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2eac478a-b120-5d42-aafd-7f3374d21918",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownH.Name",
    display_name="Unown [H]",
    searchable_by=["Unown [H]", "Basic", "UnownH"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Help]",
            game_text="Once during your turn (before your attack), if you have Unown [H], Unown [E], Unown [L], and Unown [P] on your Bench, you may shuffle your hand into your deck, then draw a new hand of the same number of cards.",
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