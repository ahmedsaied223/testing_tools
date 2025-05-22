This template provides a foundation for FIX protocol integration. Actual implementation should be customized based on specific trading system requirements and counterparty specifications.

Troubleshooting 

### **1. Basic Connectivity Checks**
**Common Issues:**
- Connection refused/timeouts
- SSL/TLS handshake failures
- Incorrect host/port configuration

**Troubleshooting Steps:**
```bash
# Network connectivity check
telnet <counterparty_host> <port>
nc -zv <counterparty_host> <port>

# SSL verification (if using TLS)
openssl s_client -connect <host>:<port> -showcerts

# Check local firewall rules
iptables -L -n
```

---

### **2. Session Layer Issues**
#### **Logon Problems (MsgType=A)**
**Common Errors:**
- `Invalid Username/Password`
- `Unsupported FIX version`
- `HeartBtInt mismatch`

**Resolution:**
1. Verify credentials in config file:
```ini
[session]
Username=YOUR_USER
Password=YOUR_PASS
```
2. Validate FIX version compatibility
3. Check HeartBtInt (must match between parties)

#### **Sequence Number Mismatches**
**Symptoms:**
- `MsgSeqNum too low/high` errors
- Gaps in message processing

**Recovery:**
```python
# Force sequence reset (use with caution)
fix.Session.reset(sessionID)
```

**Best Practice:**
```python
# Always check sequence numbers at startup
store = storefactory.create(sessionID)
next_sender = store.getNextSenderMsgSeqNum()
next_target = store.getNextTargetMsgSeqNum()
```

---

### **3. Message Parsing/Validation Errors**
**Common Failure Points:**
- Invalid tags/values
- Missing required fields
- Incorrect message structure

**Diagnostic Tools:**
```python
# Enable message validation in config
UseDataDictionary=Y
ValidateFieldsOutOfOrder=Y
ValidateFieldsHaveValues=Y

# Example error log:
# 8=FIX.4.4 | 35=D | ... | 58=Invalid tag number (1084)
```

**Resolution Workflow:**
1. Check Data Dictionary (FIX.xml) compatibility
2. Validate message structure against spec
3. Use FIX message analyzer (Wireshark/FIXInspector)

---

### **4. Application Layer Issues**
#### **Order Rejects (MsgType=8, 9)**
**Common Reasons:**
- Invalid symbol (55)
- Incorrect order type (40)
- Market closed
- Price precision errors

**Example Debugging Code:**
```python
def handleExecutionReport(message):
exec_report = fix44.ExecutionReport()
exec_report.fromMessage(message)

ord_status = exec_report.getField(fix.OrdStatus())
if ord_status in ['8', 'F']: # Rejected/Filled
print(f"Reject reason: {exec_report.getField(fix.Text())}")
```

#### **Common Field Validations:**
```python
# Check price formatting
def validate_price(price):
return round(float(price), 4) # Adjust for asset class

# Validate order type compatibility
valid_order_types = {
'EQUITY': [fix.OrdType_LIMIT, fix.OrdType_MARKET],
'FX': [fix.OrdType_LIMIT, fix.OrdType_STOP]
}
```

---

### **5. Log Analysis**
**Key Log Entries to Monitor:**
```
20240615-12:34:56.789 : Received logon request
20240615-12:35:01.123 : Sending Heartbeat
20240615-12:35:30.000 : Sequence reset received
20240615-12:36:45.678 : Application error: Invalid tag number (98)
```

**Log Pattern Matching:**
```bash
# Find session resets
grep "Received sequence reset" fix.log

# Find message rejects
grep "Reject reason" fix.log

# Monitor heartbeats
grep "Received Heartbeat" fix.log | wc -l
```

---

### **6. Common Error Scenarios**
**Scenario 1: Logon Failure**
```
8=FIX.4.4 | 35=A | 98=0 | 108=30 | 141=Y | ... | 553=bad_user | 554=wrong_pass
```
**Fix:** Verify username/password and reset sequence numbers

**Scenario 2: Invalid Message**
```
8=FIX.4.4 | 35=3 | 45=12 | 58=Invalid tag number (9999)
```
**Fix:** Update Data Dictionary and validate messages pre-send

**Scenario 3: Sequence Gap**
```
8=FIX.4.4 | 35=2 | 7=100 | 16=102 | 36=101
```
**Fix:** Initiate resend request or sequence reset

---

### **7. Tools & Resources**
1. **Protocol Analyzers:**
- Wireshark (with FIX dissector)
- FIXInspector (web-based)
- JAal (Java analyzer)

2. **Message Validation:**
```python
from quickfix import DataDictionary

dd = DataDictionary("spec/FIX44.xml")
message.validate(dd)
```

3. **Sequence Number Repair:**
```bash
# Delete sequence number files (emergency only)
rm store/*.seqnums
```

4. **Official FIX Repository:**
- [FIX Trading Community Specifications](https://www.fixtrading.org/standards/)

---

### **8. Recovery Procedures**
1. **Sequence Reset:**
```python
reset_msg = fix44.SequenceReset()
reset_msg.setField(fix.NewSeqNo(desired_seq_num))
fix.Session.sendToTarget(reset_msg, sessionID)
```

2. **Resend Request:**
```python
resend_msg = fix44.ResendRequest()
resend_msg.setField(fix.BeginSeqNo(start_seq))
resend_msg.setField(fix.EndSeqNo(end_seq))
fix.Session.sendToTarget(resend_msg, sessionID)
```

---

### **9. Testing & Validation**
**Sample Test Message (NewOrderSingle):**
```python
msg = fix44.NewOrderSingle()
msg.setField(fix.ClOrdID("ORD12345"))
msg.setField(fix.HandlInst('1'))
msg.setField(fix.Symbol("EURUSD"))
msg.setField(fix.Side(fix.Side_BUY))
msg.setField(fix.OrderQty(1000000))
msg.setField(fix.OrdType(fix.OrdType_LIMIT))
msg.setField(fix.Price(1.1200))
msg.setField(fix.TimeInForce(fix.TimeInForce_DAY))
```

**Validation Checklist:**
- [ ] All required tags present
- [ ] Numeric fields properly formatted
- [ ] Enum values match specification
- [ ] Timestamps in UTC format
- [ ] Correct decimal precision for prices/sizes

---

### **10. Best Practices**
1. Always implement:
```python
# Message checksum validation
checksum = message.checkSum()
message.getHeader().setField(checksum)
```

2. Maintain separate environments:
- Production
- UAT
- Disaster Recovery

3. Monitor key metrics:
```bash
# Message throughput
messages_per_minute=$(grep "Received" fix.log | wc -l)

# Latency measurement
sending_time=$(echo $msg | grep | 52=)
receiving_time=$(date +%s%3N)
```

4. Always coordinate with counterparty for:
- Session schedule (StartTime/EndTime)
- Planned maintenance
- Protocol upgrades

---

This structured approach covers 90% of common FIX protocol issues. For complex problems, always:
1. Capture raw network traffic
2. Compare logs with counterparty
3. Test in sandbox environment before production fixes
