is_gun_ready = bool(input())
ammo_count = int(input())

ammo_exists = ammo_count > 0

print(True if is_gun_ready and ammo_exists else False)