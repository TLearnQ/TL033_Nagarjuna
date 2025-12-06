devices = []

def api(method, path, data=None):
    if method == "GET" and path == "/items":
        return devices
    if method == "POST" and path == "/items":
        devices.append(data)
        return {"ok": True}
    return {"error": "invalid"}

print(api("POST", "/items", {"id": 101}))
print(api("GET", "/items"))