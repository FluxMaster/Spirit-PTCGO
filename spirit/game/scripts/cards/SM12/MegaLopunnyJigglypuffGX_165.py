"""STUB: effect not implemented — do not guess mechanics.
Mega Lopunny & Jigglypuff-GX (SM12 #165): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f7a44dbb-826f-521a-a624-617aac446ba9",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLopunnyJigglypuffGX.Name",
    display_name="Mega Lopunny & Jigglypuff-GX",
    searchable_by=["Mega Lopunny & Jigglypuff-GX", "Basic", "TAG TEAM", "GX", "MegaLopunnyJigglypuffGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=165,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=39,
    abilities=[
        Attack(
            title="Jumping Balloon",
            game_text="This attack does 60 more damage for each of your opponent's Pok\u00e9mon-GX and Pok\u00e9mon-EX in play.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Puffy Smashers-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep. If this Pok\u00e9mon has at least 4 extra Energy attached to it (in addition to this attack's cost), this attack does 200 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)