import requests
import sys
import concurrent.futures

def load_processed_subdomains(output_file):
    try:
        with open(output_file, "r") as output:
            return set(line.strip() for line in output)
    except FileNotFoundError:
        return set()

def request(url, output_file, processed_subdomains):
    try:
        result = requests.get("https://" + url, timeout=5)
        result.raise_for_status()

        if result.status_code == 200 and url not in processed_subdomains:
            print("[+] Subdomain discovered --->", url)
            write_to_file(output_file, url)
            processed_subdomains.add(url)
    except requests.exceptions.RequestException as e:
        pass

def write_to_file(output_file, subdomain):
    try:
        with open(output_file, "a") as output:
            output.write(subdomain + "\n")
            output.flush()
    except Exception as e:
        print("[-] Error writing to file:", e)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <target_url> <output_file>")
        sys.exit(1)

    target_url = sys.argv[1]
    output_file = sys.argv[2]

    print("Target URL:", target_url)
    print("Output File:", output_file)

    processed_subdomains = load_processed_subdomains(output_file)

    # Open subdomain list
    with open("subdomainwordlist.txt", "r") as wordlist:
        subdomains = [line.strip() for line in wordlist]

    print("Subdomains List:", subdomains)

    # Check if the output file exists, create it if not
    try:
        with open(output_file, "x"):
            pass
    except FileExistsError:
        pass

    # Use a simple loop instead of threading for troubleshooting
    for subdomain in subdomains:
        request(subdomain + "." + target_url, output_file, processed_subdomains)

if __name__ == "__main__":
    main()
