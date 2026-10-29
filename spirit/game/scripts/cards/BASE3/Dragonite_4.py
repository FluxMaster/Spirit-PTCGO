"""STUB: effect not implemented — do not guess mechanics.
Dragonite (BASE3 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="8b167c84-3db3-5088-8056-7ee083d0eae7",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="BASE3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=149,
    abilities=[
        Ability(
            title="Step In",
            game_text="Once during your turn (before your attack), if Dragonite is on your Bench, you may switch it with your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)