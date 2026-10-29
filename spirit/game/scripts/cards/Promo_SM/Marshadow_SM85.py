"""STUB: effect not implemented — do not guess mechanics.
Marshadow (Promo_SM #SM85): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="0efb5ee6-966b-5e78-b1bd-64f6623f2d0f",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshadow.Name",
    display_name="Marshadow",
    searchable_by=["Marshadow", "Basic", "Marshadow"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=802,
    abilities=[
        Ability(
            title="Let Loose",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may have each player shuffle their hand into their deck and draw 4 cards.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Punch",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)