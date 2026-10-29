"""STUB: effect not implemented — do not guess mechanics.
Celesteela-GX (SM5 #144): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="76bcfbdd-46af-5ecf-b2b3-29dedc6f4948",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CelesteelaGX.Name",
    display_name="Celesteela-GX",
    searchable_by=["Celesteela-GX", "Basic", "GX", "Ultra Beast", "CelesteelaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=144,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=797,
    abilities=[
        Attack(
            title="Rocket Fall",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Moon Press",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
        Attack(
            title="Blaster-GX",
            game_text="Turn all of your Prize cards face up. (Those Prize cards remain face up for the rest of the game.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)