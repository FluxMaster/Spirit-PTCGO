"""STUB: effect not implemented — do not guess mechanics.
Omanyte (EX12 #60): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="97da7b83-28a3-5cae-947c-4f6498e2cd8c",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    display_name="Omanyte",
    searchable_by=["Omanyte", "Stage 1", "Omanyte"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=138,
    abilities=[
        Ability(
            title="Ancient Tentacles",
            game_text="Damage done to your opponent's Pok\u00e9mon by your Omanyte, Omastar, Kabuto, Kabutops, or Kabutops ex isn't affected by Resistance.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rising Lunge",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)