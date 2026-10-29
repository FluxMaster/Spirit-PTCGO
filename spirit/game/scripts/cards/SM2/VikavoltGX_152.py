"""STUB: effect not implemented — do not guess mechanics.
Vikavolt-GX (SM2 #152): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2a6e15d2-eac3-58ce-a347-1d44883c95d9",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VikavoltGX.Name",
    display_name="Vikavolt-GX",
    searchable_by=["Vikavolt-GX", "Stage 2", "GX", "VikavoltGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=152,
    set_code="SM2",
    rarity=Rarities.RareRainbow,
    hp=240,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=738,
    abilities=[
        Attack(
            title="Charge Beam",
            game_text="Attach an Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Super Zap Cannon",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gigatron-GX",
            game_text="This attack does 60 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)