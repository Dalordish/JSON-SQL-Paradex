string = "UPDATE public.card_test SET name = 'Blinkshot', image = 'cards/fury/blinkshot.png', cost = 5, type_id = 2, affinity_id = 2, rarity_id = 5, upgrade = 3, energy_damage = null, mana_regen = null, max_health = null, physical_damage = null, health_regen = null, max_mana = null, energy_pen = null, physical_armor = null, cooldown_reduction = 0.025, physical_pen = null, energy_armor = null, crit_chance = null, lifesteal = null, crit_bonus = null, attack_speed = null, harvester_placement_time = null, max_movement_speed = null, damage_bonus = null, maxed_energy_damage = null, maxed_mana_regen = null, maxed_max_health = null, maxed_physical_damage = null, maxed_health_regen = null, maxed_max_mana = null, maxed_energy_pen = null, maxed_physical_armor = null, maxed_cooldown_reduction = null, maxed_physical_pen = null, maxed_energy_armor = null, maxed_crit_chance = null, maxed_lifesteal = null, maxed_crit_bonus = null, maxed_attack_speed = null, maxed_harvester_placement_time = null, maxed_max_movement_speed = null, maxed_damage_bonus = null, special_passive = 'Cooldown is reset on Player Kill or Assist.', special_active = 'Teleport Forward.', special_other = null, maxed_special_passive = null, maxed_special_active = null, maxed_special_other = null, enabled = 1, created_at = '2016-07-28 00:44:30.238435 +10:00', updated_at = '2016-07-28 00:44:30.238435 +10:00' WHERE name = 'Blinkshot';"

stringslist = string.split(',')
for i in range(0,len(stringslist)):
	print(stringslist[i])
