"""STUB: effect not implemented — do not guess mechanics.
Tapu Koko (SM8 #85): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="57cb581b-624b-5fbf-bbaa-3f828ae09c8a",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKoko.Name",
    display_name="Tapu Koko",
    searchable_by=["Tapu Koko", "Basic", "TapuKoko"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=785,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flashing Bolt",
            game_text="This Pok\u00e9mon can't use Flashing Bolt during your next turn.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)