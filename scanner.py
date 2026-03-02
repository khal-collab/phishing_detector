import socket

def scan_ports(target_ip, ports):
    print(f"Scanning target: {target_ip}\n")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        try:
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            else:
                print(f"[CLOSED] Port {port}")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
        finally:
            s.close()

if __name__ == "__main__":
    # Placeholder IP for demo (not a real system)
    target = "127.0.0.1"
    common_ports = [21, 22, 80, 443]

    scan_ports(target, common_ports)
