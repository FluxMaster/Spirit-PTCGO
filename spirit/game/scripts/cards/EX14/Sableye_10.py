"""STUB: effect not implemented — do not guess mechanics.
Sableye (EX14 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import amnesia


card = PokemonCardDef(
    guid="82f34cb5-f0d0-53ba-94e2-a0cfef6a511d",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=302,
    abilities=[
        Ability(
            title="Excavate",
            game_text="Once during your turn (before your attack), you may look at the top card of your deck. Put that card back on top of your deck, or discard that card. This power can't be used if Sableye is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Disable",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=amnesia,
        ),
    ],
)