# main.py

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

            