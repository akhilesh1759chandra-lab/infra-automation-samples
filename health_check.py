# Dummy Server Health Check Script
# Created for personal learning and GitHub demo purpose only

import time

def cpu_status():
    return "Normal"
--
def memory_status():
    return "Normal"

def disk_status():
    return "Normal"

def service_status():
    return "Running"

def health_report():
    print("===== Server Health Report =====")
    print("CPU Status:", cpu_status())
    print("Memory Status:", memory_status())
    print("Disk Status:", disk_status())
    print("Critical Services:", service_status())
    print("System Status: HEALTHY ✅")
    print("Last Checked:", time.ctime())
    print("================================")

health_report()
