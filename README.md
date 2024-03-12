# Subdomain_Enumeration_tool

This tool performs subdomain enumeration for a target domain using a wordlist of subdomains. It makes HTTP requests to discover valid subdomains and saves the results to an output file.

## Usage

```bash
python script.py <target_url> <output_file>
```
- `<target_url>`: The target domain for subdomain enumeration.
- `<output_file>`: The name of the output file to store discovered subdomains.

#Features
Multi-threaded subdomain enumeration for faster results.
Avoids adding duplicate subdomains to the output file.
Checks for existing processed subdomains to prevent duplicates across runs.

#Dependencies
- Python
- Requests

#Getting Started
- Install Python.

- Clone this repository:
```bash
git clone https://github.com/parvsablok/Subdomain_Enumeration_tool.git

```
- Navigate to the repository:
```bash
cd Subdomain_Enumeration_tool

```
- Install dependencies:
```bash
pip install -r requirements.txt
```
- Run the script:
```bash
python project.py example.com output.txt
```


