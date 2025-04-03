import psutil
import time

def monitor_performance():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    net_io = psutil.net_io_counters()

    print(f"CPU: {cpu_usage}% |\n MEMORY: {memory_usage}% |\n NETWORK: {net_io.bytes_sent / 1024:.2f} KB enviados, {net_io.bytes_recv / 1024:.2f} KB recebidos")

    time.sleep(5) 

import threading
monitor_thread = threading.Thread(target=monitor_performance, daemon=True)
monitor_thread.start()