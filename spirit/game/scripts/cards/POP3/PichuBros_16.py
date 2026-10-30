"""STUB: effect not implemented — do not guess mechanics.
Pichu Bros. (POP3 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fb642272-a358-586e-ad4e-5d05efe1f019",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PichuBros.Name",
    display_name="Pichu Bros.",
    searchable_by=["Pichu Bros.", "Basic", "PichuBros"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="POP3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Bustle",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads. If either coin is heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)