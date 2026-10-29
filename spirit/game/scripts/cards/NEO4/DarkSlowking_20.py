"""STUB: effect not implemented — do not guess mechanics.
Dark Slowking (NEO4 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="4eccbf9b-71fb-568c-85d8-d2bb0cdd9f52",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkSlowking.Name",
    display_name="Dark Slowking",
    searchable_by=["Dark Slowking", "Stage 1", "DarkSlowking"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=199,
    abilities=[
        Ability(
            title="Cunning",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, look at the top card of your opponent's deck. Then, you may have your opponent shuffle his or her deck. This power can't be used if Dark Slowking is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mind Shock",
            game_text="Don't apply Weakness or Resistance for this attack.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)