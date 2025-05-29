import socket
import time
from datetime import datetime

def create_fix_message(msg_type, seq_num, sender, target, body_fields=""):
    """Construct FIX message with basic headers and checksum"""
    # Standard FIX 4.4 header
    fix_header = f"8=FIX.4.4|9=0000|35={msg_type}|49={sender}|56={target}|34={seq_num}|52={datetime.utcnow().strftime('%Y%m%d-%H:%M:%S.%f')[:-3]}|"
    
    # Build complete message without checksum
    full_message = fix_header + body_fields
    body_length = len(full_message.replace("|", "\x01"))  # Calculate actual length with SOH delimiters
    full_message = full_message.replace("9=0000", f"9={body_length:04d}")
    
    # Calculate checksum (sum of all bytes mod 256)
    checksum = sum(bytearray(full_message.replace('|', '\x01'), 'ascii')) % 256
    full_message += f"10={checksum:03d}|"
    
    return full_message.replace('|', '\x01')  # Replace pipes with SOH (ASCII 1)

def parse_fix_message(fix_msg):
    """Parse FIX message into dictionary"""
    return dict(field.split('=') for field in fix_msg.split('\x01') if field)

def test_fix_rejects(host, port, sender_id, target_id):
    try:
        # Create socket connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            print(f"Connected to {host}:{port}")
            
            # Send Logon (MsgType=A)
            logon_msg = create_fix_message("A", 1, sender_id, target_id, "98=0|108=30|")
            sock.sendall(logon_msg.encode())
            print(f"Sent Logon: {logon_msg}")
            
            # Receive Logon response
            response = sock.recv(1024).decode()
            print(f"Received Logon Response: {response}")
            
            # TEST 1: Send invalid message (missing required field)
            print("\nSending malformed NewOrderSingle (missing Symbol)...")
            bad_order = create_fix_message("D", 2, sender_id, target_id, 
                "11=CLORD123|55=|54=1|38=100|40=2|44=150.75|59=0|")
            sock.sendall(bad_order.encode())
            print(f"Sent: {bad_order}")
            
            # Get Reject response
            reject1 = sock.recv(1024).decode()
            parsed_reject = parse_fix_message(reject1)
            print(f"Received Reject: {reject1}")
            
            # Validate Reject
            if parsed_reject.get('35') == '3':
                print("\n✅ Reject Received Successfully!")
                print(f"RefSeqNum: {parsed_reject.get('45')}")
                print(f"Reason: {parsed_reject.get('58')}")
            else:
                print("\n❌ Unexpected message received")
            
            # TEST 2: Send invalid message type
            print("\nSending unknown message type (Z)...")
            bad_type = create_fix_message("Z", 3, sender_id, target_id, "11=CLORD124|55=AAPL|")
            sock.sendall(bad_type.encode())
            
            reject2 = sock.recv(1024).decode()
            print(f"Received: {reject2}")
            
            # Wait before closing
            time.sleep(1)
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Configuration - Update these values
    HOST = "fix-server.example.com"  # Replace with your FIX server host
    PORT = 9876                      # Replace with your FIX server port
    SENDER_ID = "CLIENT1"
    TARGET_ID = "SERVER"
    
    test_fix_rejects(HOST, PORT, SENDER_ID, TARGET_ID)