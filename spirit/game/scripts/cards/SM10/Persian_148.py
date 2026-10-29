"""STUB: effect not implemented — do not guess mechanics.
Persian (SM10 #148): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="175b7f6d-d24f-5ee6-8188-517d158fae07",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name",
    display_name="Persian",
    searchable_by=["Persian", "Stage 1", "Persian"],
    subtypes=["Stage 1"],
    collector_number=148,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Ability(
            title="Gathering of Cats",
            game_text="Ignore all Energy in the attack costs of each of your Pok\u00e9mon in play that has the Caturday attack.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)