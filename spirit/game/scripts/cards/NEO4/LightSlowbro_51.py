"""STUB: effect not implemented — do not guess mechanics.
Light Slowbro (NEO4 #51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b374b586-dc59-5283-8d31-6e604ba96f4b",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightSlowbro.Name",
    display_name="Light Slowbro",
    searchable_by=["Light Slowbro", "Stage 1", "LightSlowbro"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=80,
    abilities=[
        Attack(
            title="Fish Out",
            game_text="Your opponent may choose up to 3 Baby Pok\u00e9mon, Basic Pok\u00e9mon, and/or Evolution cards from his or her discard pile and shuffle them into his or her deck. Either way, you may do the same.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Splash About",
            game_text="If there are more Energy attached to the Defending Pok\u00e9mon than to Light Slowbro, this attack does 20 damage plus 20 more damage. If not, this attack does 20 damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)