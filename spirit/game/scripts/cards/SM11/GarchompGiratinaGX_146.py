"""STUB: effect not implemented — do not guess mechanics.
Garchomp & Giratina-GX (SM11 #146): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack, bonus_if, has_damage


card = PokemonCardDef(
    guid="38850691-3041-5b38-98c8-b8576d6b72c5",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompGiratinaGX.Name",
    display_name="Garchomp & Giratina-GX",
    searchable_by=["Garchomp & Giratina-GX", "Basic", "TAG TEAM", "GX", "GarchompGiratinaGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=146,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=445,
    abilities=[
        Attack(
            title="Linear Attack",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=snipe_attack(40, pool='any', count=1),
        ),
        Attack(
            title="Calamitous Slash",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(has_damage(), 80),
        ),
        Attack(
            title="GG End-GX",
            game_text="Discard 1 of your opponent's Pok\u00e9mon and all cards attached to it. If this Pok\u00e9mon has at least 3 extra Fighting Energy attached to it (in addition to this attack's cost), discard 2 of your opponent's Pok\u00e9mon instead. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.FIGHTING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)