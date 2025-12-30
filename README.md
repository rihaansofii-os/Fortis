# Fortis

## Usage

Fortis is a post-exploitation research tool used to extract and validate security-relevant information **after authorized access has been obtained** during a permitted security assessment.

Navigate to the directory where Fortis is located and run the following commands:

```bash
pip install -r requirements.txt

pip3 install -r requirements.txt

python fortis.py

python3 fortis.py
```
Fortis is intended for use in authorized red team engagements, penetration tests, and controlled lab environments, focusing on responsible post-exploitation extraction and analysis.

Keywords, target directories, and extraction logic used to locate credentials or other sensitive artifacts can be modified by editing the cred_extractor.py file located inside the core/ directory.

## Disclaimer

This tool is intended strictly for educational, research, and authorized security testing purposes only.

Any use of this tool against systems, networks, or applications without explicit written permission from the owner is illegal and unethical.

The author assumes no responsibility for misuse, damage, or legal consequences resulting from the use of this tool.

By using this software, you agree that you are solely responsible for ensuring compliance with all applicable laws, regulations, and organizational policies.

For authorized red team, penetration testing, and lab environments only.

## Author

BlackHat Rihaan

