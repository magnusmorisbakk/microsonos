# main.py
from volume import handle_volume_adjustment

if __name__ == "__main__":
    while True:
        print("\n--------------------------")
        print("Sonos Controller Interface")
        print("--------------------------")
        print("[1] Adjust Volume")
        print("[Q] Quit")

        action = input("\nSelect an action: ")

        if action.upper() == "Q":
            print("Exiting interface...")
            break
        elif action == "1":
            handle_volume_adjustment()


            