"""STUB: effect not implemented — do not guess mechanics.
Exploud ex (EX14 #92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="3ab0b239-8dd7-55fb-9fb5-8da8fced4906",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exploudex.Name",
    display_name="Exploud ex",
    searchable_by=["Exploud ex", "Stage 2", "ex", "Exploudex"],
    subtypes=["Stage 2", "ex"],
    collector_number=92,
    set_code="EX14",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    family_id=293,
    abilities=[
        Ability(
            title="Extra Noise",
            game_text="As long as Exploud ex is your Active Pok\u00e9mon, put 1 damage counter on each of your opponent's Pok\u00e9mon-ex between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Derail",
            game_text="Discard a Special Energy card, if any, attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hyper Tail",
            game_text="If the Defending Pok\u00e9mon has any Pok\u00e9-Powers or Pok\u00e9-Bodies, this attack does 60 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)