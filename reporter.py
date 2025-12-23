
RESET = "\033[0m"
BOLD = "\033[1m"

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"


def report(signals, ranked):

    print(f"{CYAN}{BOLD}[*] Current User:{RESET} {GREEN}{signals.get('current_user', 'UNKNOWN')}{RESET}")
    print(f"{CYAN}{BOLD}[*] Domain Joined:{RESET} {GREEN}{signals.get('domain_joined', False)}{RESET}")

    print(f"\n{MAGENTA}{BOLD}[*] Key Signals:{RESET}")
    print(f"    {YELLOW}SeImpersonatePrivilege{RESET} : {GREEN}{signals.get('se_impersonate')}{RESET}")
    print(f"    {YELLOW}SeAssignPrimaryToken {RESET} : {GREEN}{signals.get('se_assign')}{RESET}")
    print(
        f"    {YELLOW}Credential Exposures {RESET} : "
        f"{GREEN if signals.get('cred_exposures') else RED}{bool(signals.get('cred_exposures'))}{RESET}"
    )


    exposures = signals.get("cred_exposures", [])

    if exposures:
        print(f"\n{RED}{BOLD}[!] Credential Exposure Findings (Operator Action Required):{RESET}\n")

        for item in exposures:
            print(f"    {BLUE}File   {RESET}: {item['file']}")
            print(f"    {YELLOW}Reason {RESET}: {item['reason']}")
            print(f"    {YELLOW}Impact {RESET}: {item['impact']}")
            print(f"    {CYAN}VIEW   {RESET}: type \"{item['file']}\"\n")

    
   
    print(f"\n{GREEN}{BOLD}[+] Best Attack Paths:{RESET}\n")

    if not ranked:
        print(f"{RED}[-] No high-confidence exploitation paths detected.{RESET}")
        return

    for i, p in enumerate(ranked, 1):
        print(f"{BOLD}{i}. {CYAN}{p['technique']}{RESET}")
        print(f"   {YELLOW}Impact      {RESET}: {GREEN}{p['impact']}{RESET}")
        print(f"   {YELLOW}Reliability {RESET}: {GREEN}{p['reliability']}%{RESET}")
        print(f"   {YELLOW}Noise       {RESET}: {GREEN}{p['noise']}{RESET}")
        print(f"   {YELLOW}Time        {RESET}: {GREEN}~{p['time']} min{RESET}")
        print(f"   {YELLOW}WHY         {RESET}: {p['why']}")
        print(f"   {YELLOW}CHECK       {RESET}: {p['check']}")
        print(f"   {MAGENTA}SCORE       {RESET}: {BOLD}{p['score']}{RESET}\n")
