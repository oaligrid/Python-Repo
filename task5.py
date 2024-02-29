import argparse
import platform
import psutil
import socket

# Function to get distribution information
def get_distro_info():
    return platform.platform()

# Function to get memory information
def get_memory_info():
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "used": memory.used,
        "free": memory.free
    }

# Function to get CPU information
def get_cpu_info():
    cpu_info = {}
    cpu_info["model"] = platform.processor()
    cpu_info["cores"] = psutil.cpu_count(logical=False)
    cpu_info["threads"] = psutil.cpu_count(logical=True)
    cpu_info["speed"] = psutil.cpu_freq().current
    return cpu_info

# Function to get current user information
def get_user_info():
    return platform.node()

# Function to get system load average
def get_load_average():
    return psutil.getloadavg()

# Function to get IP address
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

def main():
    parser = argparse.ArgumentParser(description='Get system information.')
    parser.add_argument('-d', '--distro', action='store_true', help='Get distribution information')
    parser.add_argument('-m', '--memory', action='store_true', help='Get memory information')
    parser.add_argument('-c', '--cpu', action='store_true', help='Get CPU information')
    parser.add_argument('-u', '--user', action='store_true', help='Get current user information')
    parser.add_argument('-l', '--load', action='store_true', help='Get system load average')
    parser.add_argument('-i', '--ip', action='store_true', help='Get IP address')

    args = parser.parse_args()

    if args.distro:
        print("Distribution Information:", get_distro_info())

    if args.memory:
        memory_info = get_memory_info()
        print("Memory Information:")
        print("Total:", memory_info['total'], "bytes")
        print("Used:", memory_info['used'], "bytes")
        print("Free:", memory_info['free'], "bytes")

    if args.cpu:
        cpu_info = get_cpu_info()
        print("CPU Information:")
        print("Model:", cpu_info['model'])
        print("Number of Cores:", cpu_info['cores'])
        print("Number of Threads:", cpu_info['threads'])
        print("CPU Speed:", cpu_info['speed'], "MHz")

    if args.user:
        print("Current User:", get_user_info())

    if args.load:
        load_average = get_load_average()
        print("Load Average (1 min, 5 min, 15 min):", load_average)

    if args.ip:
        print("IP Address:", get_ip_address())

if __name__ == "__main__":
    main()
