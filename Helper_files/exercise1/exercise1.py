import os
from Helper_files import lib

def run1():
    with open("roar.bash", "r", encoding="utf-8") as file:
        roar_script = file.read()
    with open("suspicious.bash", "r", encoding="utf-8") as file:
        sus_script = file.read()
    def createDump(contents):
        BPL = 16
        raw_bytes = contents.encode('utf-8')
        dump = []
        for i in range(0, len(raw_bytes), BPL):
            chunk = raw_bytes[i:i+BPL]
            offset = f"{i:08x}"
            hex_bytes = ' '.join(f"{b:02x}" for b in chunk)
            hex_bytes = hex_bytes.ljust(47)
            ascii_repr = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
            line = f"{offset}: {hex_bytes}  {ascii_repr}"
            dump.append(line)
        return '\n'.join(dump) + '\n'

    lib.ensure_folder_exists(
        "exercise1",
        [     
            ("Help.txt", "My script vanished! ..."),
            ("A quick RSA tutorial.txt", "Replace with actual content."),
            (".hidden_note", "Try looking into the depths..."),
            (".roar.hex", createDump(roar_script)),
            ("suspicious.bash",sus_script)
        ],
        [0o644, 0o644, 0o644, 0o644, 0o644]  # Note: initially not executable
    )
    
    # Now explicitly make 'roar' executable
    os.chmod("./exercise1/suspicious.bash", 0o755)

