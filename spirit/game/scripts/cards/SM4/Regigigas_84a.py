"""STUB: effect not implemented — do not guess mechanics.
Regigigas (SM4 #84a): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="96df9775-c78d-56c7-82a7-b7c88af5a3a5",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas", "Basic", "Regigigas"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Ability(
            title="Seal of Antiquity",
            game_text="This Pok\u00e9mon can't attack unless Regirock, Regice, and Registeel are on your Bench.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Giant Stomp",
            game_text="Discard any Stadium card in play.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=160,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)