import os
import getpass

global list_changes
list_changes = [
	['    "geo":'],
	['    "maxHealthBase":'],
	[
		'    "canDash":',
		'    "canBackDash":',
		'    "canWallJump":',
		'    "canSuperDash":',
		'    "canShadowDash":',
		'    "hasSpell":',
		'    "hasNailArt":',
		'    "hasCyclone":',
	 	'    "hasDashSlash":',
	 	'    "hasUpwardSlash":',
		'    "hasAllNailArts":',
	 	'    "hasDreamNail":',
		'    "hasDreamGate":',
		'    "hasDash":',
		'    "hasWalljump":',
		'    "hasSuperDash":',
		'    "hasShadowDash":',
		'    "hasAcidArmour":',
		'    "hasDoubleJump":',
		'    "hasLantern":',
		'    "hasTramPass":',
		'    "hasCityKey":',
		'    "hasSlykey":',
		'    "gaveSlykey":',
		'    "hasWhiteKey":',
		'    "usedWhiteKey":',
		'    "hasMenderKey":',
		'    "hasWaterwaysKey":',
		'    "hasSpaKey":',
		'    "hasLoveKey":',
		'    "hasKingsBrand":',
		'    "hasXunFlower":',
]]


def computer_name():
	return getpass.getuser()


def write_file(from_list, value, profile_id):
	file1 = open('C:/Temp/user{0}.json'.format(str(profile_id)), 'r')
	dat = file1.readlines()

	for j in from_list:
		file2 = open('C:/Temp/user{0}.json'.format(str(profile_id) + str(profile_id)), 'w')
		for i in range(len(dat)):
			if (str(dat[i]).find(j)) != -1:
				ind = (str(dat[i]).index(':')) + 1
				dat[i] = (dat[i][:ind] + ' ' + str(value) + ',\n')
			file2.write(dat[i])
		file2.close()
	file1.close()


def main_strat(value, changing, profile_id, path):
	# from .dat to .json
	if path == 'C:\\Users\\admin\\AppData\\LocalLow\\Team Cherry\\Hollow Knight':
		os.system('python hollow_knight_save_crypto.py decrypt -i "C:/Users/{1}/AppData/LocalLow/Team Cherry/Hollow Knight/user{0}.dat" -o C:/Temp/user{0}.json -v'.format(str(profile_id), computer_name()))
	else:
		os.system('python hollow_knight_save_crypto.py decrypt -i "{1}/user{0}.dat" -o C:/Temp/user{0}.json -v'.format(str(profile_id), path))


	if changing == 'geo':
		write_file(list_changes[0], value, profile_id)

	elif changing == 'maxhealth':
		write_file(list_changes[1], value, profile_id)


	elif changing == 'god_mod':
		write_file(list_changes[2], value, profile_id)


	# from .json to .dat with changes
	if path == 'C:\\Users\\admin\\AppData\\LocalLow\\Team Cherry\\Hollow Knight':
		os.system('python hollow_knight_save_crypto.py encrypt -i C:/Temp/user{0}.json -o "C:/Users/{2}/AppData/LocalLow/Team Cherry/Hollow Knight/user{1}.dat" -v'.format(str(profile_id) + str(profile_id), str(profile_id), computer_name()))
	else:
		os.system('python hollow_knight_save_crypto.py encrypt -i C:/Temp/user{0}.json -o "{2}/user{1}.dat" -v'.format(str(profile_id) + str(profile_id), str(profile_id), path))