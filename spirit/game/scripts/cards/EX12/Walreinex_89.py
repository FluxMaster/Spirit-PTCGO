"""STUB: effect not implemented — do not guess mechanics.
Walrein ex (EX12 #89): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="4f66d942-9fe0-5aea-9525-24a81b112d73",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Walreinex.Name",
    display_name="Walrein ex",
    searchable_by=["Walrein ex", "Stage 2", "ex", "Walreinex"],
    subtypes=["Stage 2", "ex"],
    collector_number=89,
    set_code="EX12",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    family_id=363,
    abilities=[
        Ability(
            title="Icy Aura",
            game_text="As long as Walrein ex is your Active Pok\u00e9mon, put 1 damage counter on each Active Pok\u00e9mon (both yours and your opponent's) between turns, excluding Water Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Water Arrow",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ice Throw",
            game_text="If the Defending Pok\u00e9mon is a Fighting Pok\u00e9mon, this attack's base damage is 120 instead of 80.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)