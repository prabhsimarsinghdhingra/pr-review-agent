import re

def parse_unified_diff(diff_text: str):
    files = []
    current = None
    lines = diff_text.splitlines()

    for i, line in enumerate(lines):
        if line.startswith("diff --git"):
            if current:
                files.append(current)

            # Extract filename
            parts = line.split(" ")
            file_path = parts[-1].replace("b/", "")
            current = {"file_path": file_path, "hunks": []}

        elif line.startswith("@@"):
            hunk = [line]
            j = i + 1
            while j < len(lines) and not lines[j].startswith("@@") and not lines[j].startswith("diff --git"):
                hunk.append(lines[j])
                j += 1
            current["hunks"].append("\n".join(hunk))

    if current:
        files.append(current)
    return files
