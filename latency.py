import requests
import time
import statistics

US_IP = "34.55.151.147"
EU_IP = "104.199.48.56"

TRIALS = 10


def measure_post(ip):
    times = []
    for i in range(TRIALS):
        start = time.time()
        requests.post(
            f"http://{ip}:8080/register",
            json={"username": f"latency-{ip}-{i}"}
        )
        times.append((time.time() - start) * 1000)
    return statistics.mean(times)


def measure_get(ip):
    times = []
    for _ in range(TRIALS):
        start = time.time()
        requests.get(f"http://{ip}:8080/list")
        times.append((time.time() - start) * 1000)
    return statistics.mean(times)


print("Measuring latency...\n")

us_reg = measure_post(US_IP)
eu_reg = measure_post(EU_IP)
us_list = measure_get(US_IP)
eu_list = measure_get(EU_IP)

print(f"US /register avg: {us_reg:.1f} ms")
print(f"EU /register avg: {eu_reg:.1f} ms")
print(f"US /list avg: {us_list:.1f} ms")
print(f"EU /list avg: {eu_list:.1f} ms")
