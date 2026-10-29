"""STUB: effect not implemented — do not guess mechanics.
Dustox (EX1 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="f5030c5c-6181-5ff6-9e4e-3ecf94327a3e",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dustox.Name",
    display_name="Dustox",
    searchable_by=["Dustox", "Stage 2", "Dustox"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Protective Dust",
            game_text="Prevent all effects of attacks, except damage, done to Dustox by the Attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Toxic",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on the Defending Pok\u00e9mon between turns.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)