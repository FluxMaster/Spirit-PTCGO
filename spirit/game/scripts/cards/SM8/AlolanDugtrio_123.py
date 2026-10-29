"""STUB: effect not implemented — do not guess mechanics.
Alolan Dugtrio (SM8 #123): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bbffa148-dfa9-566b-828f-fd95785645b1",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDugtrio.Name",
    display_name="Alolan Dugtrio",
    searchable_by=["Alolan Dugtrio", "Stage 1", "AlolanDugtrio"],
    subtypes=["Stage 1"],
    collector_number=123,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    family_id=50,
    abilities=[
        Attack(
            title="Digging Dash",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)