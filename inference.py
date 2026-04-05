import random
import time

print("[START] AI Gold Detection Environment")

tasks = ["easy", "medium", "hard"]

for task in tasks:
    print(f"[STEP] Running task: {task}")
    
    for step in range(3):
        scan_value = random.random()
        reward = round(scan_value, 2)
        print(f"[STEP] scan_step={step} reward={reward}")
        time.sleep(1)

print("[END] Inference completed successfully")
