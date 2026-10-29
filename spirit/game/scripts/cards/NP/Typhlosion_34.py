"""STUB: effect not implemented — do not guess mechanics.
Typhlosion (NP #34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="0875485a-8b33-5c49-ac3b-8cf7497cbc74",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion",
    searchable_by=["Typhlosion", "Stage 2", "Typhlosion"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=157,
    abilities=[
        Ability(
            title="Burning Aura",
            game_text="As long as Typhlosion is your Active Pok\u00e9mon, put 1 damage counter on each Active Pok\u00e9mon (both yours and your opponent's) between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flickering Flames",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rage",
            game_text="Does 50 damage plus 10 more damage for each damage counter on Typhlosion.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)