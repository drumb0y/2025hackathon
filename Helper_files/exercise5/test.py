import gibrish
# A dictionary that maps command names to a description.
import re
from gibrish import gibrish  # adjust import path if needed
commands = {
    "gibrish(int,int)": "???",
    "begin(value)": "???",
    "left()": "???",
    "right()": "???",
    "mystery(value)": "???",
    "Noname(value)": "???",
    "no()": "???",
    "yes()": "???",
    "up()": "???",
    "print()": "???",
}
variables = {}
def printCommands():
    print("\nThese are the functions available:")
    for func, desc in commands.items():
        print(f"  {func}: {desc}")
    print("\nOther commands:")
    print("  printCommands()  : Display this list again.")
    print("  update(func, desc): Update a function's description.")
    print("  exit             : Exit the program.\n")
def update(func_name, new_desc):
    global commands
    if func_name in commands:
        commands[func_name] = new_desc
        print(f"Updated description for {func_name}.")
    else:
        print(f"Function '{func_name}' not found.")
class GibrishCLI:
    def __init__(self):
        self.instances = {}

    def parse_create(self, line):
        # Matches: one = gibrish(2,2)
        pattern = r"^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*gibrish\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)\s*$"
        match = re.match(pattern, line)
        if not match:
            return None
        name, q, w = match.groups()
        return name, int(q), int(w)

    def parse_method_call(self, line):
        # Matches: instance.method(args)
        # args can be empty or a single argument (string without quotes, or int)
        pattern = r"^([a-zA-Z_][a-zA-Z0-9_]*)\.([a-zA-Z_][a-zA-Z0-9_]*)\s*\(\s*(.*?)\s*\)\s*$"
        match = re.match(pattern, line)
        if not match:
            return None
        instance_name, method_name, args_str = match.groups()
        # Parse args_str (either empty or one arg)
        args = []
        if args_str != "":
            # Try parse int else string (strip quotes if any)
            arg = args_str.strip()
            if arg.isdigit():
                args = [int(arg)]
            else:
                # Remove quotes if present
                if (arg.startswith('"') and arg.endswith('"')) or (arg.startswith("'") and arg.endswith("'")):
                    arg = arg[1:-1]
                args = [arg]
        return instance_name, method_name, args

    def run_command(self, line):
        line = line.strip()
        if not line:
            return

        if line == "exit":
            print("Goodbye.")
            exit()

        if line == "help" or line == "printCommands()":
            printCommands()
            return

        if line.startswith("update(") and line.endswith(")"):
            inside = line[len("update("):-1]
            try:
                func_name, new_desc = [x.strip().strip('\'"') for x in inside.split(",", 1)]
                update(func_name, new_desc)
            except Exception:
                print("Invalid update syntax. Use: update(func_name, new_description)")
            return

        # Try parse create instance
        created = self.parse_create(line)
        if created:
            name, q, w = created
            if name in self.instances:
                print(f"Instance '{name}' already exists.")
            else:
                try:
                    self.instances[name] = gibrish(q, w)
                    print(f"Created instance '{name}' with q={q}, w={w}")
                except Exception as e:
                    print(f"Failed to create instance '{name}': {e}")
            return

        # Try parse method call
        parsed = self.parse_method_call(line)
        if parsed:
            instance_name, method_name, args = parsed
            if instance_name not in self.instances:
                print(f"Instance '{instance_name}' not found.")
                return
            instance = self.instances[instance_name]
            try:
                if hasattr(instance, method_name):
                    method = getattr(instance, method_name)
                    method(*args)
                else:
                    print(f"Method '{method_name}' not found in instance '{instance_name}'")
            except Exception as e:
                print(f"Error: {e}")
            return

        # List or delete commands without parentheses
        parts = line.split()
        if parts[0] == "list":
            if not self.instances:
                print("No instances.")
            else:
                for name in self.instances:
                    print(f" - {name}")
            return

        if parts[0] == "delete" and len(parts) == 2:
            name = parts[1]
            if name in self.instances:
                del self.instances[name]
                print(f"Deleted instance '{name}'")
            else:
                print(f"No instance named '{name}'")
            return

        print("Unknown command. Type 'printCommands()' or 'help' for commands.")

    def repl(self):
        printCommands()  
        print("to create a new instance follow this format : name = constructor")      
        while True:
            try:
                line = input(":)")
                self.run_command(line)
            except KeyboardInterrupt:
                print("\nInterrupted. Type 'exit' to quit.")
def run(self,user_input):
       printCommands()
       while True:
            user_input = input("").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit"]:
                print("Goodbye.")
                break


            parts = user_input.split()
            cmd_name = parts[0]
            args = parts[1:]

            if hasattr(self, cmd_name):
                method = getattr(self, cmd_name)
                if callable(method):
                    try:
                        method(*args)
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    print(f"'{cmd_name}' exists but is not callable.")
            else:
                print(f"Unknown command: {cmd_name}. Type 'help' for a list.")
if __name__ == "__main__":
    cli = GibrishCLI()
    cli.repl()