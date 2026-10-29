"""STUB: effect not implemented — do not guess mechanics.
Graveler (NEO3 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage


card = PokemonCardDef(
    guid="aef0bf25-16ac-5002-ac72-d5d27ca1860a",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    display_name="Graveler",
    searchable_by=["Graveler", "Stage 1", "Graveler"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Earthquake",
            game_text="Does 10 damage to each of your own Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=spread_damage(10, side='mine', also_base=True),
        ),
        Attack(
            title="Rock Tumble",
            game_text="Don't apply Resistance.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)