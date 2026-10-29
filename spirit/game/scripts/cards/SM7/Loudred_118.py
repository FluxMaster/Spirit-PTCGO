"""STUB: effect not implemented — do not guess mechanics.
Loudred (SM7 #118): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="087039a9-f7e2-5bba-8d87-f2566438bc53",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    display_name="Loudred",
    searchable_by=["Loudred", "Stage 1", "Loudred"],
    subtypes=["Stage 1"],
    collector_number=118,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Cracking Voice",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)