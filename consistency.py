import requests
import time

US_IP = "34.55.151.147"
EU_IP = "104.199.48.56"

TRIALS = 10
not_found = 0

for i in range(TRIALS):
    username = f"consistency-{i}"

    # write to US
    requests.post(
        f"http://{US_IP}:8080/register",
        json={"username": username}
    )

    # immediately read from EU
    res = requests.get(f"http://{EU_IP}:8080/list")

    if username not in res.text:
        print(f"Trial {i+1}: NOT FOUND")
        not_found += 1
    else:
        print(f"Trial {i+1}: FOUND")

    time.sleep(1)

print("\n========= RESULT =========")
print(f"Total trials: {TRIALS}")
print(f"Username NOT found: {not_found} times")
