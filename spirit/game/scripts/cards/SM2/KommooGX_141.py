"""STUB: effect not implemented — do not guess mechanics.
Kommo-o-GX (SM2 #141): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d775f260-9423-5cb6-adeb-5c2f2ad58d26",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KommooGX.Name",
    display_name="Kommo-o-GX",
    searchable_by=["Kommo-o-GX", "Stage 2", "GX", "KommooGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=141,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    family_id=782,
    abilities=[
        Attack(
            title="Adamantine Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ultra Uppercut-GX",
            game_text="(You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=240,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)