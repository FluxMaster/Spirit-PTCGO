"""STUB: effect not implemented — do not guess mechanics.
Dark Scizor (NEO4 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="43ae2cfd-512d-535e-b804-c5118c468a9f",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkScizor.Name",
    display_name="Dark Scizor",
    searchable_by=["Dark Scizor", "Stage 1", "DarkScizor"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Attack(
            title="Threaten",
            game_text="Flip a coin. If heads, look at your opponent's hand. If he or she has any Trainer cards there, choose 1 of them. Your opponent shuffles that card into his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)