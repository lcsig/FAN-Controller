#!/usr/bin/env python3
import os
import sys

# Embedded Controller File
EC_IO_FILE = "/sys/kernel/debug/ec/ec0/io"


def is_root():
    return os.geteuid() == 0


def load_ec_module():
    if not os.path.exists(EC_IO_FILE):
            os.system("modprobe ec_sys write_support=1")


def ec_write(addr, value):
    with open(EC_IO_FILE, "rb") as f:
        f.seek(addr)
        old_value = ord(f.read(1))

    if value != old_value:
        print("[+] Changed \t---> %3d @ %3d => %3d " % (old_value, addr, value))
        with open(EC_IO_FILE, "wb") as f:
            f.seek(addr)
            f.write(bytearray([value]))
    else:
        print("[+] No Change \t---> %3d @ %3d" % (value, addr))


if __name__ == "__main__":

    # Root Check
    if not is_root():
        print("[!] Run it as a root!")
        exit()

    # Load EC Module
    load_ec_module()

    # Check for Input File
    if len(sys.argv) == 1:
        print(f"[!] No profile was passed into script")
        exit(1)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"[!] Could not find {input_file}")
        exit(1)

    # Write
    for line in open(input_file).readlines():
        if line.startswith(">WEC"):
            addr, value = line.split()[1:3]
            ec_write(int(addr, 0), int(value, 0))
        elif "_" in line:
            print("[#]")
            print(f"[+] ---> {line[1:-2]}")
