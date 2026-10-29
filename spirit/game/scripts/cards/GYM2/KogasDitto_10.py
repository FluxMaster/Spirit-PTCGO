"""STUB: effect not implemented — do not guess mechanics.
Koga's Ditto (GYM2 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae785192-4ed3-50af-9176-967039d0485e",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasDitto.Name",
    display_name="Koga's Ditto",
    searchable_by=["Koga's Ditto", "Basic", "KogasDitto"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=132,
    abilities=[
        Attack(
            title="Giant Growth",
            game_text="Flip a coin. If heads, Koga's Ditto's maximum HP is now 80 and Koga's Ditto's Pound attack's base damage is 30 instead of 10. (Benching Koga's Ditto ends this effect.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)