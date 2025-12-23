import subprocess
import os
import getpass

from core.cred_extractor import extract_credentials


def run(cmd):
    try:
        return subprocess.check_output(
            cmd,
            shell=True,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL
        ).decode(errors="ignore").strip()
    except:
        return ""


def collect_signals():
    signals = {}

    signals["current_user"] = (
        run("whoami")
        or getpass.getuser()
        or os.environ.get("USERNAME", "UNKNOWN")
    )

    signals["privs"] = run("whoami /priv")
    signals["groups"] = run("whoami /groups")

    signals["se_impersonate"] = "SeImpersonatePrivilege" in signals["privs"]
    signals["se_assign"] = "SeAssignPrimaryTokenPrivilege" in signals["privs"]

    
    signals["uac"] = run(
        "reg query HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA"
    )

    signals["domain_joined"] = bool(
        run("wmic computersystem get domain | findstr /i /v Domain")
    )

    signals["cred_exposures"] = extract_credentials()

    return signals

