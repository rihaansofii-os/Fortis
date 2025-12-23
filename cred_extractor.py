import os
import re

KEYWORDS = [
    "password",
    "passwd",
    "pass",
    "code",
    "passcode",
    "important",
    "pwd",
    "secret",
    "apikey",
    "api_key",
    "db_password"
]

FILE_EXTENSIONS = [".xml", ".ini", ".config", ".yml", ".yaml", ".env", ".txt"]

SEARCH_PATHS = [
    "C:\\ProgramData",
    "C:\\Users\\Public",
    "C:\\Windows\\Panther",
    "C:\\inetpub",
    "C:\\xampp",
    "C:\\wamp",
    "C:\\Users\\",
]

def is_interesting_file(filename):
    return any(filename.lower().endswith(ext) for ext in FILE_EXTENSIONS)

def contains_secret(content):
    for k in KEYWORDS:
        if re.search(rf"{k}\s*[:=]", content, re.IGNORECASE):
            return True
    return False

def extract_credentials():
    findings = []

    for base in SEARCH_PATHS:
        if not os.path.exists(base):
            continue

        for root, _, files in os.walk(base):
            for file in files:
                if not is_interesting_file(file):
                    continue

                full_path = os.path.join(root, file)

                try:
                    if os.path.getsize(full_path) > 2 * 1024 * 1024:
                        continue  

                    with open(full_path, "r", errors="ignore") as f:
                        content = f.read()

                    if contains_secret(content):
                        findings.append({
                            "file": full_path,
                            "reason": "Readable file contains credential-like keywords",
                            "impact": "Possible credential exposure"
                        })

                except:
                    continue

    return findings
