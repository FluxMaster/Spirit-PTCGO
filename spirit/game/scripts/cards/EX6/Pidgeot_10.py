"""STUB: effect not implemented — do not guess mechanics.
Pidgeot (EX6 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="31484bcd-cf88-52f8-b35a-ed7e57655185",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name",
    display_name="Pidgeot",
    searchable_by=["Pidgeot", "Stage 2", "Pidgeot"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="EX6",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=16,
    abilities=[
        Ability(
            title="Quick Search",
            game_text="Once during your turn (before your attack), you may choose any 1 card from your deck and put it into your hand. Shuffle your deck afterward. You can't use more than 1 Quick Search Pok\u00e9-Power each turn. This power can't be used if Pidgeot is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Clutch",
            game_text="The Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=condition_attack(no_retreat=True),
        ),
    ],
)