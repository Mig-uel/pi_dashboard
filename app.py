from flask import Flask, render_template
import psutil
import socket
import time

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    # System info
    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    uptime_seconds = time.time() - psutil.boot_time()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    temps = psutil.sensors_temperatures()
    cpu_temp = None

    if 'cpu_thermal' in temps:
        cpu_temp = temps['cpu_thermal'][0].current


    return render_template("index.html",
                           cpu=cpu_percent,
                           mem_total=mem.total // (1024*1024),
                           mem_used=mem.used // (1024*1024),
                           mem_percent=mem.percent,
                           disk_total=disk.total // (1024*1024*1024),
                           disk_used=disk.used // (1024*1024*1024),
                           disk_percent=disk.percent,
                           uptime=int(uptime_seconds // 60),
                           hostname=hostname,
                           ip=ip_address,
                           cpu_temp=cpu_temp
                           )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)