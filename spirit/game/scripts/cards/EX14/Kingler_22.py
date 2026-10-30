"""STUB: effect not implemented — do not guess mechanics.
Kingler δ (EX14 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1df793f8-ddc8-5bd3-93af-da828a0e1e9d",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingler.Name",
    display_name="Kingler δ",
    searchable_by=["Kingler \u03b4", "Stage 1", "Kingler"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="EX14",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name",
    family_id=98,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Prop-up Pinchers",
            game_text="If Kingler has a Pok\u00e9mon Tool card attached to it, this attack does 40 damage plus 40 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)