import os

ENTRY = "Our 15-minute standup ran 47 minutes because the build took 13 and my update took the other 34."

if not 1 <= len(ENTRY) <= 200:
    raise SystemExit(f"entry must be 1-200 chars, got {len(ENTRY)}")
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
print(f"wrote {len(ENTRY)} chars")
