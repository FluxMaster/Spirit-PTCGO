"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Alakazam (GYM2 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ebf2e589-dc05-5ad3-a75e-48f04b52685f",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasAlakazam.Name",
    display_name="Sabrina's Alakazam",
    searchable_by=["Sabrina's Alakazam", "Stage 2", "SabrinasAlakazam"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasKadabra.Name",
    family_id=63,
    abilities=[
        Ability(
            title="Psylink",
            game_text="Sabrina's Alakazam always has a copy of every attack your Psychic Pok\u00e9mon in play have (including their Energy costs and anything else required in order to use those attacks, such as discarding Energy cards). This power can't be used if Sabrina's Alakazam is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mega Burn",
            game_text="You can't use this attack during your next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)