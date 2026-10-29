"""STUB: effect not implemented — do not guess mechanics.
Lucario (Promo_SM #SM54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="119639d7-4187-5c70-bd50-acb8c52488d7",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=448,
    abilities=[
        Ability(
            title="Stance",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may prevent all effects of your opponent's attacks, including damage, done to this Pok\u00e9mon until the end of your opponent's next turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Submarine Blow",
            cost={PokemonTypes.FIGHTING: 3},
            damage=120,
        ),
    ],
)