"""STUB: effect not implemented — do not guess mechanics.
Torracat (SM10 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="722de152-e386-5081-a193-02b64eba7246",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    display_name="Torracat",
    searchable_by=["Torracat", "Stage 1", "Torracat"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name",
    family_id=725,
    abilities=[
        Attack(
            title="Fire Fang",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)