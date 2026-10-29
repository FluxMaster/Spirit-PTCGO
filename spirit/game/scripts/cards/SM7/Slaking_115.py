"""STUB: effect not implemented — do not guess mechanics.
Slaking (SM7 #115): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ba81e28a-ce77-5e8a-90ba-60b52eae308f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2", "Slaking"],
    subtypes=["Stage 2"],
    collector_number=115,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Lazy",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Pok\u00e9mon in play have no Abilities, except for Lazy.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Critical Move",
            game_text="Discard an Energy from this Pok\u00e9mon. It can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)