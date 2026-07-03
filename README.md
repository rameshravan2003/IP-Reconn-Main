Specter - Web-Based Reconnaissance & Network Analysis Tool

Specter is a comprehensive, web-based reconnaissance tool built with Python and Flask. It consolidates the functionality of multiple network analysis and OSINT (Open-Source Intelligence) tools into a single, user-friendly interface. This project is designed to streamline the initial phase of any network investigation by providing a holistic and organized report on a given target.

In addition to its on-demand scanning capabilities, Specter also includes a real-time traffic analyzer and a basic network attack monitor.

## Key Features
Specter provides a wide range of information-gathering modules:

On-Demand Reconnaissance Tool:

📍 Geolocation & ISP Lookup: Identifies the physical location of an IP address with an interactive map.

🚦 IP Reputation & Blacklist Check: Queries the AbuseIPDB API to check for malicious activity reports.

🚀 Open Port Scanning: Scans for common open TCP ports to identify running services.

🌐 HTTP Header Analysis: Fetches and displays HTTP headers from web servers to identify software and security configurations.

📄 DNS Record Enumeration: Retrieves A, AAAA, MX, NS, and TXT records.

🔎 Subdomain Discovery: Scans for common subdomains associated with a target domain.

👤 WHOIS Lookup: Fetches public registration data for both domain names and IP addresses.

🛡️ SSL/TLS Certificate Analysis: Inspects a website's SSL certificate for issuer, subject, and validity details.

Live Traffic Analyzer:

🔴 Real-Time Monitoring: Captures and displays live network traffic from your machine in a structured, color-coded table.

TCP Flag Analysis: Shows TCP flags (SYN, ACK, etc.) for deeper insight into network connections.

Target Filtering: Allows you to filter the live traffic view to only show packets related to a specific IP or domain.

Malicious Connection Alerts: Actively monitors outbound traffic and generates a security alert if a connection is made to a known malicious IP address.

## Technology Stack
Backend: Python 3, Flask

Frontend: HTML, CSS, JavaScript, Jinja2

UI Framework: Bootswatch (Vapor Theme for Bootstrap 5)

Key Python Libraries:

Flask, Flask-WTF: Web server and forms.

requests: For all HTTP API calls.

scapy: For live packet sniffing.

dnspython: For DNS lookups.

python-whois & ipwhois: For WHOIS lookups.

python-dotenv: For managing environment variables.

External APIs:

ip-api.com for geolocation.

abuseipdb.com for IP reputation.

## Setup and Usage
### 1. Prerequisites
Python 3.8+

A Python virtual environment

### 2. Installation
Clone the repository:

Bash

git clone <your-repo-url>
cd <your-repo-folder>
Create and activate a virtual environment:

Bash

# On Windows
python -m venv myenv
.\myenv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install the required Python packages:

Bash

pip install -r requirements.txt
### 3. Configuration
Get API Key: Sign up for a free account at abuseipdb.com and create an API key.

Create .env file: In the root project directory, create a file named .env.

Add Key: Add your API key to the .env file:

ABUSEIPDB_API_KEY='your_key_here'
### 4. Running the Application
This project has two main components that must be run separately.

To use the Recon Tool (Web Scanner):

Run the Flask web server in your terminal:

Bash

python run.py
Open your browser and navigate to http://127.0.0.1:5000.

To use the Live Traffic Analyzer:

First, run the web server as described above (python run.py).

Second, open a new terminal as an Administrator.

On Windows: Right-click your Terminal/PowerShell icon and select "Run as administrator."

On macOS/Linux: Use the sudo command.

In the new admin terminal, navigate to your project folder, activate the virtual environment, and run the analyzer script:

Bash

# (Activate your environment first)
python live_analyzer.py

Navigate to the "Live Traffic Analyzer" page on the web interface to see the output.
<img width="1912" height="927" alt="Screenshot 2025-09-02 152727" src="https://github.com/user-attachments/assets/9c7ce364-b197-45cc-b9fa-f83e670fb371" />
<img width="1917" height="927" alt="Screenshot 2025-09-02 152828" src="https://github.com/user-attachments/assets/6cd0c5ad-75c7-4338-852b-69255f9c3252" />
<img width="1887" height="921" alt="Screenshot 2025-09-02 152948" src="https://github.com/user-attachments/assets/8720da41-7d83-4795-bbee-b8cd2abd3ae1" />
