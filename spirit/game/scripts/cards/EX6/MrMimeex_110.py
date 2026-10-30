"""STUB: effect not implemented — do not guess mechanics.
Mr. Mime ex (EX6 #110): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="529a6440-f191-552b-adf0-22b115ce174d",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMimeex.Name",
    display_name="Mr. Mime ex",
    searchable_by=["Mr. Mime ex", "Basic", "ex", "MrMimeex"],
    subtypes=["Basic", "ex"],
    collector_number=110,
    set_code="EX6",
    rarity=Rarities.RareHoloEX,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=122,
    abilities=[
        Ability(
            title="Magic Odds",
            game_text="If Mr. Mime ex would be damaged by an attack, prevent that attack's damage done to Mr. Mime ex if that damage is 10, 30, 50, 70, 90, 110, 130, 150, or 170.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Breakdown",
            game_text="Count the number of cards in your opponent's hand. Put that many damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)