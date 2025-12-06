messages = ["hello", "bad{json", "world"]
log = []
fail = 0

for m in messages:
    try:
        log.append(m.encode())
    except:
        fail += 1

print("Log:", log)
print("Failed:", fail)