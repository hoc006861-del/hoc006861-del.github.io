import os

ROOT_DIR = "."
OUTPUT_FILE = "index.html"

def generate():
    links = []

    for root, dirs, files in os.walk(ROOT_DIR):
        # bỏ các folder không cần
        dirs[:] = [d for d in dirs if d not in [".git", ".github"]]

        for file in files:
            if file.endswith(".html") and file != "index.html":
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, ROOT_DIR)
                links.append(rel_path.replace("\\", "/"))

    links.sort()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Index</title>
</head>
<body>
<h1>My Pages</h1>
<ul>
""")

        for link in links:
            f.write(f'<li><a href="{link}">{link}</a></li>\n')

        f.write("""
</ul>
</body>
</html>
""")

if __name__ == "__main__":
    generate()
