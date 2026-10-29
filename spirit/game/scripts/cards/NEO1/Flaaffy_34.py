"""STUB: effect not implemented — do not guess mechanics.
Flaaffy (NEO1 #34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aa6d46eb-fd75-5062-80e8-d40366530f37",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    display_name="Flaaffy",
    searchable_by=["Flaaffy", "Stage 1", "Flaaffy"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Discharge",
            game_text="Discard all Lightning Energy cards attached to Flaaffy in order to use this attack. Flip a number of coins equal to the number of Lightning Energy cards you discarded. This attack does 30 damage times then number of heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Electric Current",
            game_text="Take 1 Lightning Energy cards attached to Flaaffy and attach it to 1 of your Benched Pok\u00e9mon. If you have no Benched Pok\u00e9mon, discard that Energy card.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)