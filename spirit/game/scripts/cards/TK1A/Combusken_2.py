"""STUB: effect not implemented — do not guess mechanics.
Combusken (TK1A #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="edf74467-cbff-5a12-91e0-f4f2df9c5cf1",
    key="TK1A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    display_name="Combusken",
    searchable_by=["Combusken", "Stage 1", "Combusken"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="TK1A",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Double Kick",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)