"""STUB: effect not implemented — do not guess mechanics.
Necrozma-GX (SM3 #134): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="c55bcf55-4cdb-5000-8ce8-b6c17346f535",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NecrozmaGX.Name",
    display_name="Necrozma-GX",
    searchable_by=["Necrozma-GX", "Basic", "GX", "NecrozmaGX"],
    subtypes=["Basic", "GX"],
    collector_number=134,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=800,
    abilities=[
        Ability(
            title="Light's End",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from Colorless Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Prismatic Burst",
            game_text="Discard all Psychic Energy from this Pok\u00e9mon. This attack does 60 more damage for each card you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Black Ray-GX",
            game_text="This attack does 100 damage to each of your opponent's Pok\u00e9mon-GX and Pok\u00e9mon-EX. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)