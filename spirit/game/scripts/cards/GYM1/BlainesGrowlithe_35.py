"""STUB: effect not implemented — do not guess mechanics.
Blaine's Growlithe (GYM1 #35): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="af4b5285-23d5-5020-a706-871de63db032",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesGrowlithe.Name",
    display_name="Blaine's Growlithe",
    searchable_by=["Blaine's Growlithe", "Basic", "BlainesGrowlithe"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Shake",
            game_text="If your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with the Defending Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Fire Tackle",
            game_text="Blaine's Growlithe does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)