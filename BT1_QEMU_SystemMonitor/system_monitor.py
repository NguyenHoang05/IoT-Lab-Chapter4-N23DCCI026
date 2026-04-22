import psutil
from datetime import datetime
from time import sleep

log_file = open('system_log.txt', 'w')

try:
    while True:
        # CPU
        cpu_list = psutil.cpu_percent(interval=1, percpu=True)
        cpu_avg = sum(cpu_list) / len(cpu_list)

        # RAM
        ram = psutil.virtual_memory()
        ram_used_mb = ram.used // (1024**2)
        ram_total_mb = ram.total // (1024**2)
        ram_pct = ram.percent

        # Disk
        disk = psutil.disk_usage('/')
        disk_pct = disk.percent

        # Cảnh báo
        if cpu_avg >= 70:
            status = 'CRITICAL'
        elif cpu_avg >= 30:
            status = 'WARNING'
        else:
            status = 'NORMAL'

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Dòng log dài được ngắt thành 2 dòng để không vượt quá 120 ký tự
        line = (f'[{now}] CPU: {cpu_avg:.1f}% | RAM: {ram_used_mb}/{ram_total_mb} MB '
                f'({ram_pct}%) | Disk: {disk_pct}% | {status}')
        print(line)
        log_file.write(line + '\n')
        log_file.flush()

        if status != 'NORMAL':
            print(f' ⚠ {status}: CPU đang ở {cpu_avg:.1f}%')

        sleep(2)

except KeyboardInterrupt:
    print('\nDừng giám sát.')
finally:
    log_file.close()
    print('Log saved to system_log.txt')
