"""STUB: effect not implemented — do not guess mechanics.
Mewtwo & Mew-GX (Promo_SM #SM191): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="993b69c4-fb1a-5dd7-83d7-388231994727",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoMewGX.Name",
    display_name="Mewtwo & Mew-GX",
    searchable_by=["Mewtwo & Mew-GX", "Basic", "TAG TEAM", "GX", "MewtwoMewGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=191,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Ability(
            title="Perfection",
            game_text="This Pok\u00e9mon can use the attacks of any Pok\u00e9mon-GX or Pok\u00e9mon-EX on your Bench or in your discard pile. (You still need the necessary Energy to use each attack.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Miraculous Duo-GX",
            game_text="If this Pok\u00e9mon has at least 1 extra Energy attached to it (in addition to this attack's cost), heal all damage from all of your Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)