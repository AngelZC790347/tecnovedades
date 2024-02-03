import re
import subprocess
import json
if __name__ == '__main__':
    res = subprocess.run(["ls"], capture_output=True)
    res2 = list(filter(lambda r: re.search("-700x700.webp$", r), res.stdout.decode().split("\n")))
    json = json.dumps([{"name": image[:-13], "imageUrl":image, "description":"", "clientUrl":""} for image in res2])
    with open("../../portafolio.json", "w") as f:
        f.write(json)
