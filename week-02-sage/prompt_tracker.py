# prompt-tracker.py - A simple tool to manage your AI prompts

def show_menu():
    """Prints the main menu options to the console."""
    print("\n--- AI PROMPT TRACKER ---")
    print("1. Add Prompt")
    print("2. View Prompts")
    print("3. Search Prompts")
    print("4. Delete Prompt") # New option!
    print("5. Quit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        # --- ADD PROMPT ---
        text = input("Enter the prompt: ")
        category = input("Enter category (learning/creating/evaluating/other): ").lower()
        note = input("Short note on when to use it: ")

        # We open the file in 'a' (append) mode so we don't erase old prompts.
        # We join the fields with '|' so we can split them easily later.
        with open("my-prompts.txt", "a") as f:
            f.write(f"{category}|{text}|{note}\n")
        print("Prompt saved!")

    elif choice == "2":
        # --- VIEW PROMPTS ---
        print("\n--- ALL SAVED PROMPTS ---")
        try:
            with open("my-prompts.txt", "r") as f:
                for line in f:
                    # strip() removes the newline character at the end
                    # split("|") breaks the line into a list
                    category, p_text, p_note = line.strip().split("|")
                    print(f"[{category.upper()}]")
                    print(f"Prompt: {p_text}")
                    print(f"Note: {p_note}")
                    print("-" * 20)
        except FileNotFoundError:
            print("No prompts saved yet! Add one first.")

    elif choice == "3":
        # --- SEARCH PROMPTS ---
        keyword = input("Search for keyword: ").lower()
        found = False
        
        try:
            with open("my-prompts.txt", "r") as f:
                for line in f:
                    if keyword in line.lower():
                        category, p_text, p_note = line.strip().split("|")
                        print(f"\nMatch Found in [{category}]:")
                        print(f"Prompt: {p_text}")
                        found = True
            
            if not found:
                print("No matches found.")
        except FileNotFoundError:
            print("File not found. Try adding a prompt first!")

    elif choice == "4":
        # --- DELETE PROMPT ---
        try:
            # Step 1: Read all current prompts into a list
            with open("my-prompts.txt", "r") as f:
                lines = f.readlines()

            if not lines:
                print("Nothing to delete.")
                continue

            # Show the user the list so they can pick a number
            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")

            delete_idx = int(input("Enter the number of the prompt to delete: ")) - 1

            if 0 <= delete_idx < len(lines):
                # Step 2: Remove the chosen item from our list
                removed = lines.pop(delete_idx)
                
                # Step 3: Write the list back to the file (overwriting the old file)
                with open("my-prompts.txt", "w") as f:
                    f.writelines(lines)
                print(f"Deleted: {removed.strip()}")
            else:
                print("Invalid number.")

        except (FileNotFoundError, ValueError):
            print("Error: Could not delete. Make sure you entered a valid number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please pick 1-5.")