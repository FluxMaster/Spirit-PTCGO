"""STUB: effect not implemented — do not guess mechanics.
Erika's Vileplume (GYM1 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="29e59cf5-b8a6-5e7e-96e7-0a6c4099bdcb",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasVileplume.Name",
    display_name="Erika's Vileplume",
    searchable_by=["Erika's Vileplume", "Stage 2", "ErikasVileplume"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasGloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Pollen Defense",
            game_text="If an attack does damage to Erika's Vileplume while it's your Active Pok\u00e9mon (even if it's Knocked Out), flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused. This power works even while Erika's Vileplume is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mega Drain",
            game_text="If Erika's Vileplume does damage to the Defending Pok\u00e9mon (after applying Weakness and Resistance), remove a number of damage counters from Erika's Vileplume equal to half the damage done to the Defending Pok\u00e9mon (rounded up to the nearest 10). If Erika's Vileplume has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)