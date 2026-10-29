"""STUB: effect not implemented — do not guess mechanics.
Normalium Z: Tackle (SM11 #203): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If the Pokémon this card is attached to has the Tackle attack, it can use the GX attack on this card. (You still need the necessary Energy to use this attack.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import BARRELING_BLITZ_GX

card = PokemonToolCardDef(guid='e0e79950-9af0-52af-b325-ef747d9ba488', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.NormaliumZTackle.Name', display_name='Normalium Z: Tackle', searchable_by=['Normalium Z: Tackle', 'Pokémon Tool'], subtypes=['Pokémon Tool'], collector_number=203, set_code='SM11', rarity=Rarities.Uncommon, granted_abilities=[BARRELING_BLITZ_GX])
