"""STUB: effect not implemented — do not guess mechanics.
Aggron (EX1 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0af1e14c-e1c9-50f4-8169-cd350d50a3dc",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name",
    display_name="Aggron",
    searchable_by=["Aggron", "Stage 2", "Aggron"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Retaliate",
            game_text="Flip a coin. If heads, this attack does 10 damage times the number of damage counters on Aggron.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
        Attack(
            title="Double Lariat",
            game_text="Flip 2 coins. This attack does 70 damage times the number of heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)