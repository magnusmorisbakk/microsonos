# volume.py

def handle_volume_adjustment():
    while True:
        action = input("\nSet volume level (0-100) or [B] to go back: ")

        if action.upper() == "B":
            break
        elif action.isdigit() and 0 <= int(action) <= 100:
            volume_level = int(action)
            set_volume_level(volume_level)
            print(f"Volume set to {volume_level}.")
