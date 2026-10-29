"""STUB: effect not implemented — do not guess mechanics.
Togepi & Cleffa & Igglybuff-GX (SM12 #143): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d6e369a2-16d2-52f5-87ec-6c754c526889",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TogepiCleffaIgglybuffGX.Name",
    display_name="Togepi & Cleffa & Igglybuff-GX",
    searchable_by=["Togepi & Cleffa & Igglybuff-GX", "Basic", "TAG TEAM", "GX", "TogepiCleffaIgglybuffGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=143,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=173,
    abilities=[
        Attack(
            title="Rolling Panic",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Supreme Puff-GX",
            game_text="Take another turn after this one. (Skip the between-turns step.) If this Pok\u00e9mon has at least 14 extra Fairy Energy attached to it (in addition to this attack's cost), your opponent shuffles all of their Benched Pok\u00e9mon and all cards attached to them into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)