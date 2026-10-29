"""STUB: effect not implemented — do not guess mechanics.
Volcanion (SM10 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9e93702-4707-51e2-a847-fd8f5f01a474",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name",
    display_name="Volcanion",
    searchable_by=["Volcanion", "Basic", "Volcanion"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Attack(
            title="Flare Starter",
            game_text="Search your deck for a Fire Energy card and attach it to 1 of your Pok\u00e9mon. If you go second and it's your first turn, instead search for up to 3 Fire Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="High-Heat Blast",
            game_text="If you have at least 4 Fire Energy in play, this attack does 60 more damage.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)