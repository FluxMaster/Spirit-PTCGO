"""STUB: effect not implemented — do not guess mechanics.
Carnivine (SM5 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7474acc6-a814-562c-af73-96de2f2aa9b8",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic", "Carnivine"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=455,
    abilities=[
        Attack(
            title="Chomp Chomp",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Loom Over",
            game_text="This attack does 10 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=90,
            damage_operator="-",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)