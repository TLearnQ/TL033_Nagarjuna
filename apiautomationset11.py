log = []
attempts = 0
success = False

while attempts < 3:
    attempts += 1
    log.append(f"Attempt {attempts}")

    if attempts == 3:
        success = True
        log.append("Success")
        break

print(log)


