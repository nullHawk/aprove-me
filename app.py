import subprocess
import threading
import time

def run_backend():
    subprocess.run(["python", "backend/app.py"])

def run_frontend():
    time.sleep(2)  # Let Flask start up first
    subprocess.run(["streamlit", "run", "frontend/app.py", "--server.port=7860", "--server.address=0.0.0.0"])

if __name__ == "__main__":
    t1 = threading.Thread(target=run_backend)
    t2 = threading.Thread(target=run_frontend)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
