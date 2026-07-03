import datetime
import os
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

# --- Define the absolute path for the log file ---
# Gets the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "traffic.log")

def packet_callback(packet):
    """
    This function is called for every packet and logs a summary to a file.
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = ""
    
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        if TCP in packet:
            flags = packet[TCP].flags
            log_entry = f"[{timestamp}] TCP: {src_ip}:{packet[TCP].sport} -> {dst_ip}:{packet[TCP].dport} [Flags: {flags}]"
        elif UDP in packet:
            log_entry = f"[{timestamp}] UDP: {src_ip}:{packet[UDP].sport} -> {dst_ip}:{packet[UDP].dport}"
        elif ICMP in packet:
            log_entry = f"[{timestamp}] ICMP: {src_ip} -> {dst_ip} (Type: {packet[ICMP].type})"
        
        if log_entry:
            # Write the formatted entry to the log file
            with open(LOG_FILE, "a") as f:
                f.write(log_entry + "\n")
            print(log_entry) # Also print to the console

if __name__ == '__main__':
    # Clear the log file on start
    with open(LOG_FILE, "w") as f:
        f.write(f"--- Live Traffic Log Initialized at {datetime.datetime.now()} ---\n")

    print("🚀 Starting live traffic analyzer...")
    print(f"Logging traffic to: {LOG_FILE}")
    print("Press CTRL+C to stop.")
    sniff(prn=packet_callback, store=0)