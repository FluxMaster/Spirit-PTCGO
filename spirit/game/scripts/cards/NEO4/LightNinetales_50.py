"""STUB: effect not implemented — do not guess mechanics.
Light Ninetales (NEO4 #50): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7f2bc2c8-ecae-56ca-a686-d67e77430077",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightNinetales.Name",
    display_name="Light Ninetales",
    searchable_by=["Light Ninetales", "Stage 1", "LightNinetales"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Guiding Flame",
            game_text="Put a Baby Pok\u00e9mon or a Basic Pok\u00e9mon card from your discard pile onto your Bench. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard a Fire Energy card attached to Light Ninetales in order to use this attack.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)