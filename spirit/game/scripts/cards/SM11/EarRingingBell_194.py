"""STUB: effect not implemented — do not guess mechanics.
Ear-Ringing Bell (SM11 #194): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If the Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if that Pokémon is Knocked Out), the Attacking Pokémon is now Confused.
  - You may play as many Item cards as you like during your turn (before your attack).
"""
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import EAR_RINGING_BELL_ABILITIES

card = PokemonToolCardDef(guid='2d77f5bb-b373-5265-8b33-6902f10fffe8', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.EarRingingBell.Name', display_name='Ear-Ringing Bell', searchable_by=['Ear-Ringing Bell', 'Pokémon Tool'], subtypes=['Pokémon Tool'], collector_number=194, set_code='SM11', rarity=Rarities.Uncommon, granted_abilities=EAR_RINGING_BELL_ABILITIES)
