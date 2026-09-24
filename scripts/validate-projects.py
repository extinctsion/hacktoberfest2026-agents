from pathlib import Path

REQUIRED_FIELDS = [
    "**GitHub:**",
    "**Category:**",
    "**Language:**",
    "**License:**",
]

ROOT_DIR = Path(__file__).resolve().parents[1]

markdown_files = list(ROOT_DIR.glob("agents/*.md"))

errors = []

for file in markdown_files:
    content = file.read_text(encoding="utf-8")

    for field in REQUIRED_FIELDS:
        if field not in content:
            errors.append(f"{file}: missing {field}")

if errors:
    print("Validation failed:\n")

    for error in errors:
        print(f"- {error}")

    raise SystemExit(1)

print("All project files passed validation.")