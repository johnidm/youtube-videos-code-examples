import psutil
import platform
from datetime import datetime

def get_system_info():
    print("="*50)
    print("SYSTEM INFORMATION")
    print("="*50)
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

def get_cpu_info():
    print("\n" + "="*50)
    print("CPU INFORMATION")
    print("="*50)
    
    # CPU cores
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def get_memory_info():
    print("\n" + "="*50)
    print("MEMORY INFORMATION")
    print("="*50)
    
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    
    print("\nSWAP MEMORY")
    print("-"*20)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def monitor_resources(duration=10, interval=1):
    print("\n" + "="*50)
    print(f"MONITORING RESOURCES FOR {duration} SECONDS")
    print("="*50)
    print(f"{'Time':<20} {'CPU %':<10} {'Memory %':<12} {'Memory Used':<15}")
    print("-" * 60)
    
    for _ in range(duration):
        current_time = datetime.now().strftime("%H:%M:%S")
        cpu_percent = psutil.cpu_percent(interval=interval)
        memory = psutil.virtual_memory()
        
        print(f"{current_time:<20} {cpu_percent:<10.1f} {memory.percent:<12.1f} {get_size(memory.used):<15}")

def get_process_info():
    print("\n" + "="*50)
    print("TOP 10 PROCESSES BY CPU USAGE")
    print("="*50)
    
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    processes = sorted(processes, key=lambda x: x['cpu_percent'] or 0, reverse=True)[:10]
    
    print(f"{'PID':<10} {'Name':<25} {'CPU %':<10} {'Memory %':<10}")
    print("-" * 60)
    for proc in processes:
        print(f"{proc['pid']:<10} {proc['name'][:24]:<25} {proc['cpu_percent'] or 0:<10.1f} {proc['memory_percent'] or 0:<10.1f}")

def main():
    print(f"Resource Monitor - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    get_system_info()
    get_cpu_info()
    get_memory_info()
    get_process_info()


if __name__ == "__main__":
    main()