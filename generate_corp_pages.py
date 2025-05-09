import os
import re

CORP_FOLDERS = ["A Corps", "AA Corps", "AAA Corps", "Corps (Local)"]
OUTPUT_DIR = "output"

def fix_markdown_bullets(text):
    output_lines = []

    for line in text.splitlines():
        # Normalize tabs → 4 spaces
        line = line.replace("\t", "    ")
        match = re.match(r'^(\s*)([-*+])\s+(.*)', line)

        if match:
            indent = match.group(1)
            content = match.group(3)

            level = max(1, len(indent) // 4 + 1)  # 4 spaces = 1 level
            output_lines.append(f"{'*' * level} {content}")
        else:
            output_lines.append(line)

    return "\n".join(output_lines)


def convert_markdown_to_mediawiki(text):
    # Bullet points
    text = fix_markdown_bullets(text)
    # Headers
    text = re.sub(r'###### (.+)', r'====== \1 ======', text)
    text = re.sub(r'##### (.+)', r'===== \1 =====', text)
    text = re.sub(r'#### (.+)', r'==== \1 ====', text)
    text = re.sub(r'### (.+)', r'=== \1 ===', text)
    text = re.sub(r'## (.+)', r'== \1 ==', text)
    text = re.sub(r'# (.+)', r'= \1 =', text)

    # Bold and italics
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r"'''\1'''", text)  # bold+italic
    text = re.sub(r'\*\*(.+?)\*\*', r"'''\1'''", text)
    text = re.sub(r'\*(.+?)\*', r"''\1''", text)

    # Lists
    # Replace all leading dashes with appropriate number of asterisks based on indentation
    text = re.sub(r'^([ \t]*)(- )', lambda m: ' ' * len(m.group(1)) + '*' * (len(m.group(1)) // 2 + 1) + ' ', text, flags=re.MULTILINE)

    # Markdown links → MediaWiki links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'[[\2|\1]]', text)

    return text


def flatten_links(text):
    return re.sub(r'\[\[(?:\.\./)*([^|\]]+)(?:\|([^\]]+))?\]\]', lambda m: f"[[{m.group(1)}|{m.group(2) or m.group(1)}]]", text)

def extract_tags(text):
    return set(re.findall(r"#([A-Za-z0-9_\-/]+)", text))

def is_division(name):
    return any(k in name.lower() for k in ["factory", "office", "division", "plant", "lab"])

def detect_corp_rating(folder_name):
    folder_name = folder_name.lower()
    if "aaa" in folder_name:
        return "AAA Corp"
    elif "aa" in folder_name:
        return "AA Corp"
    elif "a corp" in folder_name:
        return "A Corp"
    else:
        return "National Corp"  # fallback

def format_as_division(title, body):
    out = f"== {title} ==\n\n"
    if "District:" in body or "Country:" in body:
        lines = body.splitlines()
        for line in lines:
            if "District:" in line:
                out += f"===== District: {line.split('District:')[1].strip()} =====\n"
            elif "Country:" in line:
                out += f"===== Country: {line.split('Country:')[1].strip()} =====\n"
        remaining = "\n".join([l for l in lines if not l.startswith("District:") and not l.startswith("Country:")])
        out += "\n" + remaining
    else:
        out += body
    return out

def format_as_corp(title, body):
    lines = [line for line in body.splitlines() if line.strip()]
    
    if not lines:
        return f"<p>No description available.</p>\n\n= Divisions =\n\n<!-- Add divisions here -->"

    intro_paragraph = lines[0]
    rest = "\n".join(lines[1:]).strip()

    result = f"<p>{intro_paragraph}</p>\n\n= Divisions =\n\n"
    if rest:
        result += rest + "\n"
    else:
        result += "<!-- Add divisions here -->\n"

    return result



def format_file(filepath, filename, corp_rating):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    content = flatten_links(content)
    tags = extract_tags(content)
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    body = "\n".join([l for l in lines if not l.lower().startswith("source:")])
    body = convert_markdown_to_mediawiki(body)


    base = os.path.splitext(filename)[0]

    if is_division(base):
        result = format_as_division(base, body)
    else:
        result = format_as_corp(base, body)

    result += f"\n\n[[Category:{corp_rating}]]\n"
    for tag in sorted(tags):
        result += f"[[Category:{tag.replace('_', ' ')}]]\n"

    return result

# === MAIN ===
for top_folder in CORP_FOLDERS:
    if not os.path.isdir(top_folder):
        continue

    corp_rating = detect_corp_rating(top_folder)

    for root, dirs, files in os.walk(top_folder):
        for file in files:
            if not file.endswith(".md"):
                continue

            full_path = os.path.join(root, file)
            relative_dir = os.path.relpath(root, start=top_folder)
            sub_output_dir = os.path.join(OUTPUT_DIR, top_folder, relative_dir)
            os.makedirs(sub_output_dir, exist_ok=True)

            output_text = format_file(full_path, file, corp_rating)

            out_filename = os.path.splitext(file)[0] + ".txt"
            out_path = os.path.join(sub_output_dir, out_filename)

            with open(out_path, "w", encoding="utf-8") as out_file:
                out_file.write(output_text)

            print(f"✅ Wrote: {out_path}")

