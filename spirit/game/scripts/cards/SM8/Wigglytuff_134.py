"""STUB: effect not implemented — do not guess mechanics.
Wigglytuff (SM8 #134): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="bd9cd9c3-6ee3-58e5-8dbe-2db28ed9c248",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name",
    display_name="Wigglytuff",
    searchable_by=["Wigglytuff", "Stage 1", "Wigglytuff"],
    subtypes=["Stage 1"],
    collector_number=134,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Attack(
            title="Expand",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Charmed Slap",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool card that has \"Fairy Charm\" in its name attached to it, this attack does 70 more damage.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)