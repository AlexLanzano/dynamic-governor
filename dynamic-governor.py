#!/usr/bin/env python3
import time
import subprocess

# Threshold for switching to performance mode
LOAD_THRESHOLD = 6.0

# Interval between checks (seconds)
CHECK_INTERVAL = 10

def get_loadavg():
    """Return the 1-minute load average as a float."""
    with open("/proc/loadavg") as f:
        load = float(f.read().split()[0])
    return load

def get_current_governor():
    """Return the current CPU governor of CPU0."""
    try:
        result = subprocess.check_output(
            ["cpupower", "frequency-info", "-p"],
            stderr=subprocess.DEVNULL
        ).decode()
        # Example output: "analyzing CPU 0:\n  current policy: frequency should be within ..."
        # Not directly giving governor, so fallback:
        result = subprocess.check_output(
            ["cat", "/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        return result
    except subprocess.CalledProcessError:
        return None

def set_governor(mode):
    """Set CPU governor across all CPUs."""
    print(f"[+] Switching governor to: {mode}")
    subprocess.run(["sudo", "cpupower", "frequency-set", "-g", mode], check=False)

def main():
    print(f"[*] Starting auto governor control")
    while True:
        current_governor = get_current_governor()
        if not current_governor:
            print("[-] Could not detect current governor.")
            return

        load = get_loadavg()
        print(f"[Load] {load:.2f}")

        if load > LOAD_THRESHOLD and current_governor != "performance":
            set_governor("performance")
            current_governor = "performance"

        elif load <= LOAD_THRESHOLD and current_governor != "powersave":
            set_governor("powersave")
            current_governor = "powersave"

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
