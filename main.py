
import json

fin = open('input.txt', 'r')
fout = open('output.txt','w')

content = fin.read()
parsed_json = json.loads(content)

type_id = {
	'Passive' : 1,
	'Active' : 2,
	'Upgrade' : 3,
	'Prime' : 4,
	'Acitve/Passive' : 5
}

affinity_id = {
	'Intellect' : 1,
	'Fury' : 2,
	'Corruption' : 3,
	'Order' : 4,
	'Growth' : 5,
	'Universal' : 6,
	'Prime' : 7,
	'(Removed)' : 8
}

rarity_id = {
	'Starter' : 1,
	'Uncommon' : 2,
	'Common' : 3,
	'Rare' : 4,
	'Epic' : 5
}

def genCom(item,value):
	string =' ' + item + '=' + '\'' +  str(value) + '\''
	return(string)
'''
for item in parsed_json:
	for effects in item['effects']:
		print(effects.keys())
'''

for item in parsed_json:
	command = []
	command.append('UPDATE')
	command.append(' public.card_test SET')
	command.append(genCom('name',item['name']))
	command.append(genCom('cost',item['cost']))
	command.append(genCom('type',type_id[item['type']]))
	command.append(genCom('affinity_id',affinity_id[item['affinity']]))
	command.append(genCom('upgrade',item['upgradeSlots']))
	for effects in item['effects']:
		if 'stat' in effects:
			command.append(genCom('placeholder_effect_' + effects['stat'],effects['value']))
		elif 'passive' in effects:
			command.append(genCom('special_passive',effects['description']))
		elif 'cooldown' in effects:
			command.append(genCom('special_active',effects['description']))
			command.append(genCom('placeholder_cooldown',effects['cooldown']))
	command.append(' WHERE name = \'' + item['name'] + '\'')
	strcommand = ''.join(command)
	print strcommand
	print('')