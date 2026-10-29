"""STUB: effect not implemented — do not guess mechanics.
Dark Typhlosion (NEO4 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e46dbeea-cd74-5f71-8678-1c5c3670c677",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkTyphlosion.Name",
    display_name="Dark Typhlosion",
    searchable_by=["Dark Typhlosion", "Stage 2", "DarkTyphlosion"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkQuilava.Name",
    family_id=155,
    abilities=[
        Attack(
            title="Claw Swipe",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Rushing Flames",
            game_text="You may discard any number of Fire Energy cards attached to your Pok\u00e9mon. Flip a coin for each Fire Energy card discarded in this way. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)