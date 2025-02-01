commands = {
    "help": "help", "h": "help", "?": "help",
    "exit": "exit", "e": "exit",
    "create": "create", "c": "create",
    "load": "load", "l": "load",
    "save": "save", "s": "save",
    "show": "show", "sh": "show"
}


user_input = input("> ").lower()

if user_input in commands:
    print(commands[user_input])
else:
    print("Invalid command")
