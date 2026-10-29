"""STUB: effect not implemented — do not guess mechanics.
Feraligatr (ECARD1 #47): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="3c1d2607-2d12-5524-895f-e63ed2c2110c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=47,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Major Tsunami",
            game_text="Once during your turn (before your attack), if Feraligatr is your Active Pok\u00e9mon and if your opponent has any Benched Pok\u00e9mon, your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon. Either way, if you have any Benched Pok\u00e9mon, switch Feraligatr with 1 of them. This power can't be used if Feraligatr is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rending Jaws",
            game_text="If here are no damage counters on the Defending Pok\u00e9mon, this attack's base damage is 40 instead of 70.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)