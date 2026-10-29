"""STUB: effect not implemented — do not guess mechanics.
Amoonguss (Promo_SM #SM202): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="c1b103fa-1e60-57c3-adae-1783b1253b9d",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name",
    display_name="Amoonguss",
    searchable_by=["Amoonguss", "Stage 1", "Amoonguss"],
    subtypes=["Stage 1"],
    collector_number=202,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    family_id=591,
    abilities=[
        Ability(
            title="Bursting Spores",
            game_text="Whenever you play a Pok\u00e9mon that has the Spore attack from your hand during your turn, you may leave your opponent's Active Pok\u00e9mon Asleep and Poisoned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)