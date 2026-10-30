"""STUB: effect not implemented — do not guess mechanics.
Shiftry ex (EX14 #97): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="67892294-7033-5622-ac7d-ee25f26169f7",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftryex.Name",
    display_name="Shiftry ex",
    searchable_by=["Shiftry ex", "Stage 2", "ex", "Shiftryex"],
    subtypes=["Stage 2", "ex"],
    collector_number=97,
    set_code="EX14",
    rarity=Rarities.RareHoloEX,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Ability(
            title="Dark Eyes",
            game_text="After your opponent's Pok\u00e9mon uses a Pok\u00e9-Power, put 2 damage counters on that Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Target Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. If that Pok\u00e9mon already has any damage counters on it, this attack does 50 damage instead. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Blade Arms",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)