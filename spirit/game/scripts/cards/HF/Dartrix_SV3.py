"""STUB: effect not implemented — do not guess mechanics.
Dartrix (HF #SV3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d290428a-c848-5e65-958b-0458b78a5ef9",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    display_name="Dartrix",
    searchable_by=["Dartrix", "Stage 1", "Dartrix"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="HF",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name",
    family_id=722,
    abilities=[
        Attack(
            title="Sharp Blade Quill",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Leaf Blade",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)