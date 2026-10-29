"""STUB: effect not implemented — do not guess mechanics.
Kommo-o (DM #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f29b8957-fccd-5b55-86b5-5c3d66b28add",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kommoo.Name",
    display_name="Kommo-o",
    searchable_by=["Kommo-o", "Stage 2", "Kommoo"],
    subtypes=["Stage 2"],
    collector_number=54,
    set_code="DM",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    family_id=782,
    abilities=[
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Raging Uppercut",
            game_text="If this Pok\u00e9mon has 8 or more damage counters on it, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)