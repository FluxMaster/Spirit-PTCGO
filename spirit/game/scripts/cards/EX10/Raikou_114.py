"""STUB: effect not implemented — do not guess mechanics.
Raikou ★ (EX10 #114): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import smash_turn

card = PokemonCardDef(
    guid="96f6bc55-128e-50bf-b26c-5780d8ba3b4e",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou ★",
    searchable_by=["Raikou \u2605", "Basic", "Star", "Raikou"],
    subtypes=["Basic", "Star"],
    collector_number=114,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Attack(
            title="Lightning Turn",
            game_text="Switch Raikou Star with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=smash_turn(),
        ),
        Attack(
            title="Meta Voltage",
            game_text="If you have less Prize cards left than your opponent, this attack does 40 damage to each of your Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)