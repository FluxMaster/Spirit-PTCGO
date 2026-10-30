"""STUB: effect not implemented — do not guess mechanics.
Machoke (EX12 #39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="76ef0b3e-4f37-5397-b9f0-c43f6a1423c3",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    display_name="Machoke",
    searchable_by=["Machoke", "Stage 1", "Machoke"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Paranoid",
            game_text="As long as Machoke is Confused, Machoke's attacks do 50 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Split Kick",
            game_text="Does 20 damage to each Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Magnum Punch",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)