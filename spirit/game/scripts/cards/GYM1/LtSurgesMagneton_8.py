"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Magneton (GYM1 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="9bb34757-f2f7-578f-a2b9-eb8a93066f6a",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesMagneton.Name",
    display_name="Lt. Surge's Magneton",
    searchable_by=["Lt. Surge's Magneton", "Stage 1", "LtSurgesMagneton"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesMagnemite.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Energy Charge",
            game_text="As often as you like during your turn (before your attack), if Lt. Surge's Magneton is your Active Pok\u00e9mon, you may take 1 Lightning Energy card attached to 1 of your Pok\u00e9mon and attach it to Lt. Surge's Magneton. This power can't be used if Lt. Surge's Magneton is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mega Shock",
            game_text="Flip a coin. If tails, Lt. Surge's Magneton does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)