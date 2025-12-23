from core.collector_win import collect_signals
from core.rules_win import evaluate_rules
from core.scorer import score_paths
from core.reporter import report
import sys
import time
import threading


def animated_loader(text="Collecting system signals"):
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    stop_event = threading.Event()

    def run():
        i = 0
        while not stop_event.is_set():
            sys.stdout.write(f"\r{text} {spinner[i % len(spinner)]}")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1

        sys.stdout.write("\r" + " " * 100 + "\n")
        sys.stdout.flush()

    t = threading.Thread(target=run, daemon=True)
    t.start()
    return stop_event

def banner():
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    print(f"""{BLUE}{BOLD}
███████╗ ██████╗ ██████╗ ████████╗██╗███████╗
██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝██║██╔════╝
█████╗  ██║   ██║██████╔╝   ██║   ██║███████╗
██╔══╝  ██║   ██║██╔══██╗   ██║   ██║╚════██║
██║     ╚██████╔╝██║  ██║   ██║   ██║███████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝
{RESET}
{CYAN}{BOLD}FORTIS{RESET}  {GREEN}Internal Offensive Security Framework{RESET}

{YELLOW}Author   :{RESET} BlackHatRihaan (https://www.linkedin.com/in/rihaan-sofi)
{YELLOW}Scope    :{RESET} Red Team Operations | Adversary Emulation | OSCE-Level Workflows
{RED}{BOLD}Notice   :{RESET} Authorized use only. Intended for controlled, ethical security testing.

{CYAN}-----------------------------------------------------------------------------------------------------------------------------------------{RESET}
""")


def main():
    banner()

    loader = animated_loader("Collecting system signals")
    signals = collect_signals()
    
    loader.set()

    paths = evaluate_rules(signals)
    ranked = score_paths(paths)
    report(signals, ranked)


if __name__ == "__main__":
    main()
