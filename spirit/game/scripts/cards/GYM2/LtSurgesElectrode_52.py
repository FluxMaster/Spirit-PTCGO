"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Electrode (GYM2 #52): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ba6253d1-6666-51c7-bbe7-9e85025bb572",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesElectrode.Name",
    display_name="Lt. Surge's Electrode",
    searchable_by=["Lt. Surge's Electrode", "Stage 1", "LtSurgesElectrode"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesVoltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Shock Blast",
            game_text="If Lt. Surge's Electrode is your Active Pok\u00e9mon and gets damaged (even if it's Knocked Out), flip a coin. If tails, this power does 20 damage to each Active Pok\u00e9mon. This power works even if Lt. Surge's Electrode is already Asleep, Confused, or Paralyzed when it takes damage.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Power Ball",
            game_text="Flip 3 coins. This attack does 30 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)