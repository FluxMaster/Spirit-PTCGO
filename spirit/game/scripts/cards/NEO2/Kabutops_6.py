"""STUB: effect not implemented — do not guess mechanics.
Kabutops (NEO2 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1cd590b5-d823-54a4-84f1-ab677443c69d",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name",
    display_name="Kabutops",
    searchable_by=["Kabutops", "Stage 2", "Kabutops"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="NEO2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    family_id=140,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Hydrocutter",
            game_text="Flip a number of coins equal to the number of Energy cards attached to Kabutops. This attack does 40 damage times the number of heads. You can't flip more than 3 coins in this way.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)