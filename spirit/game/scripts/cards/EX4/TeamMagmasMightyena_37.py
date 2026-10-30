"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Mightyena (EX4 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="01ee1298-503c-5a34-aadb-cac44fc34778",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasMightyena.Name",
    display_name="Team Magma's Mightyena",
    searchable_by=["Team Magma's Mightyena", "Stage 1", "TeamMagmasMightyena"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasPoochyena.Name",
    family_id=261,
    abilities=[
        Ability(
            title="Call for Help",
            game_text="Once during your turn (before your attack), if Team Magma's Mightyena is your Active Pok\u00e9mon, you may search your deck for a Pok\u00e9mon with Team Magma in its name, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Team Magma's Mightyena is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lunge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)