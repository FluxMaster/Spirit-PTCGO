"""STUB: effect not implemented — do not guess mechanics.
Golisopod (SM11 #51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import bonus_if


card = PokemonCardDef(
    guid="bdc28478-cc70-5ac2-9dca-0dc2b9e2de0f",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golisopod.Name",
    display_name="Golisopod",
    searchable_by=["Golisopod", "Stage 1", "Golisopod"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Ability(
            title="Emergency Exit",
            game_text="If this Pok\u00e9mon has 2 or fewer Energy attached to it, it has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="First Impression",
            game_text="If this Pok\u00e9mon was on the Bench and became your Active Pok\u00e9mon this turn, this attack does 60 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(lambda ctx: ctx.entered_active_this_turn(ctx.attacker), 60),
        ),
    ],
)