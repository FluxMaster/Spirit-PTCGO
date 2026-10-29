"""STUB: effect not implemented — do not guess mechanics.
Unown [F] (NEO2 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="b8c93e96-9970-5fdf-8b08-df87a3906714",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownF.Name",
    display_name="Unown [F]",
    searchable_by=["Unown [F]", "Basic", "UnownF"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Find]",
            game_text="Once during your turn (before your attack), if you have Unown [F], Unown [I], Unown [N], and Unown [D] on your Bench, you may search your deck for a Trainer card. Show that card to your opponent, then put it into your hand. Shuffle your deck afterward.",
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