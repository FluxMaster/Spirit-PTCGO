"""STUB: effect not implemented — do not guess mechanics.
Armaldo ex (EX12 #84): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="aaeb9054-d7e8-503b-9695-77266c1f5b78",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armaldoex.Name",
    display_name="Armaldo ex",
    searchable_by=["Armaldo ex", "Stage 2", "ex", "Armaldoex"],
    subtypes=["Stage 2", "ex"],
    collector_number=84,
    set_code="EX12",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    family_id=347,
    abilities=[
        Ability(
            title="Dual Armor",
            game_text="As long as Armaldo ex has any React Energy cards attached to it, Armaldo ex is both Grass and Fighting type.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Spiral Drain",
            game_text="Remove 2 damage counters from Armaldo ex.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Vortex Chop",
            game_text="If the Defending Pok\u00e9mon has any Resistance, this attack's base damage is 100 instead of 70.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)