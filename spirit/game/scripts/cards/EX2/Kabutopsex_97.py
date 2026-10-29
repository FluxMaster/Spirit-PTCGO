"""STUB: effect not implemented — do not guess mechanics.
Kabutops ex (EX2 #97): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="628bd3bb-a3c2-51b2-9409-2c432f057530",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabutopsex.Name",
    display_name="Kabutops ex",
    searchable_by=["Kabutops ex", "Stage 2", "ex", "Kabutopsex"],
    subtypes=["Stage 2", "ex"],
    collector_number=97,
    set_code="EX2",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    family_id=140,
    abilities=[
        Attack(
            title="Hydrocutter",
            game_text="Flip a number of coins equal to the amount of Energy attached to Kabutops ex. This attack does 40 damage times the number of heads. You can't flip more than 3 coins in this way.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Spiral Drain",
            game_text="Remove 2 damage counters from Kabutops ex (remove 1 if there is only 1).",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)