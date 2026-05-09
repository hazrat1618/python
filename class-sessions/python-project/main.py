import platform
import shutil
import os
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/system-info")
def get_system_info():
    try:
        return {
            "platform": platform.platform(),
            "architecture": platform.architecture(),
            "version": platform.version()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/disk-usage")
def check_disk_usage(path: str = "/"):
    total, used, free = shutil.disk_usage(path)
    return {
        "total_gib": total // (2**30),
        "used_gib": used // (2**30),
        "free_gib": free // (2**30)
    }

@app.get("/list-directory")
def list_directory(path: str = "./"):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_directory(full_path)
        else:
            print(full_path)

@app.get("/ping")
def ping_host(hostname: str):
    param = '-n' if os.sys.platform == 'win32' else '-c'
    response = os.system(f"ping {param} 1 {hostname}")
    if response == 0:
        return {"hostname": hostname, "status": "up"}
    else:
        return {"hostname": hostname, "status": "down"}
