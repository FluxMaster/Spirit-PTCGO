"""STUB: effect not implemented — do not guess mechanics.
Regirock ex (EX5 #98): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="e6ce22fa-c51b-5e0c-8829-229080dc0e84",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirockex.Name",
    display_name="Regirock ex",
    searchable_by=["Regirock ex", "Basic", "ex", "Regirockex"],
    subtypes=["Basic", "ex"],
    collector_number=98,
    set_code="EX5",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=377,
    abilities=[
        Ability(
            title="Healing Stone",
            game_text="At any time between turns, remove 1 damage counter from Regirock ex.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Tonnage",
            game_text="You may do 60 damage plus 20 more damage. If you do, Regirock ex does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)