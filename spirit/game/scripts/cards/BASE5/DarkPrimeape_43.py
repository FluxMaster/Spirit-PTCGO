"""STUB: effect not implemented — do not guess mechanics.
Dark Primeape (BASE5 #43): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="d034d073-5446-5d3e-8b8c-0b2cfe55a37e",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPrimeape.Name",
    display_name="Dark Primeape",
    searchable_by=["Dark Primeape", "Stage 1", "DarkPrimeape"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Ability(
            title="Frenzy",
            game_text="If Dark Primeape does any damage while it's Confused (even to itself), it does 30 more damage.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Frenzied Attack",
            game_text="Dark Primeape is now Confused (after doing damage).",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)