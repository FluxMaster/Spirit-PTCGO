"""STUB: effect not implemented — do not guess mechanics.
Unown [G] (NEO4 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ff13f30a-b67b-5e1e-b73f-0117615c86cf",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownG.Name",
    display_name="Unown [G]",
    searchable_by=["Unown [G]", "Basic", "UnownG"],
    subtypes=["Basic"],
    collector_number=27,
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
            title="[Give]",
            game_text="Once during your turn (before your attack), if you have Unown [G], Unown [I], Unown [V], and Unown [E] on your Bench, you may flip a coin. If heads, search your deck for a basic Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
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