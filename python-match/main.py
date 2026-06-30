
def main():
    point = (1, 1)
    
    match point:
        case (x, y) if x == y:
            print("on the diagonal")
        case (x, y) if x > 0 and y > 0:
            print("first quadrant")
        case (x, y):
            print("somewhere else")

    # command = ["get", "https://httpbin.org/get"]

    # match command:
    #     case (("get" | "fetch"), url):
    #         print(f"Fetching {url}")
    #     case ("post", url, data):
    #         print(f"Posting to {url} with data {data}")

    # config = {"debug": False, "output": "file.txt", "format": "xml"}
    # match config:
    #     case {"debug": True}:
    #         print("Debug mode enabled")
    #     case {"output": path, "format": "json"}:
    #         print(f"Output to {path} in JSON format")
    #     case {"output": path, **rest}:
    #         print(f"Output to {path} - {rest}")
    # command = [1, 2]
    # match command:
    #     case []:
    #         print("empty")
    #     case [single]:
    #         print(f"one item: {single}")
    #     case [first, second]:
    #         print(f"two items: {first}, {second}")
    #     case [first, *rest]:
    #         print(f"first is {first}, then {len(rest)} more")

    # point = (1, 2)
    # match point:
    #     case (0, 0):
    #         print("Origin")
    #     case (x, 2):
    #         print(f"X={x}, Y={y}")
    #     case _:
    #         raise ValueError("Not a point")

    # response = requests.get("https://httpbin.org/get")
    # result = {"status_code": response.status_code, "data": response.json()}

    # match result:
    #     case {"status_code": 200, "data": data}:
    #         print("Success", data)
    #     case {"status_code": 404, "data": data}:
    #         print("Not Found", data)
    #     case {"status_code": 500}:
    #         print("Internal Server Error")
    #     case {"status_code": status}:
    #         raise ValueError(f"Unknown status: {status}")
    
    # status_code = response.status_code
    # match status_code:
    #     case 200:
    #         print("OK")
    #     case 201:
    #         print("Created")
    #     case 404:
    #         print("Not Found")
    #     case 500:
    #         print("Internal Server Error")
    #     case _:
    #         print("Unknown Status Code")


if __name__ == "__main__":
    main()