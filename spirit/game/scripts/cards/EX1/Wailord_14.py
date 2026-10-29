"""STUB: effect not implemented — do not guess mechanics.
Wailord (EX1 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6495c703-f896-5de9-ad57-aee498df6790",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailord.Name",
    display_name="Wailord",
    searchable_by=["Wailord", "Stage 1", "Wailord"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    family_id=320,
    abilities=[
        Attack(
            title="Take Down",
            game_text="Wailord does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)