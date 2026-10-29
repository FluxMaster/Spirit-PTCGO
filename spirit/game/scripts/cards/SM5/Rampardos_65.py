"""STUB: effect not implemented — do not guess mechanics.
Rampardos (SM5 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="11f0b89a-1a36-56bf-b13e-d0e0b89868f1",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rampardos.Name",
    display_name="Rampardos",
    searchable_by=["Rampardos", "Stage 2", "Rampardos"],
    subtypes=["Stage 2"],
    collector_number=65,
    set_code="SM5",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    family_id=408,
    abilities=[
        Attack(
            title="Clean Hit",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Wild Crash",
            game_text="If your opponent's Active Pok\u00e9mon is a Basic Pok\u00e9mon, it is Knocked Out.",
            cost={PokemonTypes.FIGHTING: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)