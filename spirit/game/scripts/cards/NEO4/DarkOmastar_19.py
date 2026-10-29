"""STUB: effect not implemented — do not guess mechanics.
Dark Omastar (NEO4 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8093d8b4-f282-53cb-8777-2ce65b43f042",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkOmastar.Name",
    display_name="Dark Omastar",
    searchable_by=["Dark Omastar", "Stage 2", "DarkOmastar"],
    subtypes=["Stage 2"],
    collector_number=19,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkOmanyte.Name",
    family_id=138,
    abilities=[
        Attack(
            title="Prehistoric Water",
            game_text="If your opponent has any evolved Pok\u00e9mon in play, choose 1 of them and flip a coin. If heads, your opponent takes the highest Stage Evolution card on that Pok\u00e9mon and shuffles it into his or her deck.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dark Tentacle",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't evolve except from effects of attacks or Pok\u00e9mon Powers. (Benching that Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)