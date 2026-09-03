import re, glob, sys

files = glob.glob("*.html")
if not files:
    print("No .html files found in current directory. cd into your repo folder first.")
    sys.exit(1)

pattern = re.compile(
    r'<div class="ad-banner-wrap">.*?</script>\s*',
    re.DOTALL
)

changed = []
for f in files:
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
    new_content, n = pattern.subn("", content)
    if n > 0:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(new_content)
        changed.append((f, n))

if changed:
    print("Removed ad banner blocks from:")
    for f, n in changed:
        print(f"  {f}: {n} block(s) removed")
else:
    print("No ad-banner-wrap blocks found — nothing changed.")
