import socket
from datetime import datetime

# Take inputs
target = input("Enter target IP address (e.g. 127.0.0.1): ").strip()
start_port = int(input("Enter starting port (e.g. 20): ").strip())
end_port = int(input("Enter ending port (e.g. 80): ").strip())

# Start scan
print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
start_time = datetime.now()

for port in range(start_port, end_port + 1):
    try:
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"✅ Port {port} is OPEN")
        else:
            print(f"❌ Port {port} is CLOSED")

        sock.close()
    except Exception as e:
        print(f"⚠️ Error on port {port}: {e}")

end_time = datetime.now()
print(f"\n⏱️ Scan finished in: {end_time - start_time}")
