"""Genera íconos PNG mínimos para el PWA."""
import struct, zlib

def make_png(size, color=(124, 111, 239)):
    r, g, b = color
    def chunk(name, data):
        c = name + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)
    ihdr = struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0)
    raw = b''.join(b'\x00' + bytes([r, g, b] * size) for _ in range(size))
    return (b'\x89PNG\r\n\x1a\n' +
            chunk(b'IHDR', ihdr) +
            chunk(b'IDAT', zlib.compress(raw)) +
            chunk(b'IEND', b''))

from pathlib import Path
Path('icon-192.png').write_bytes(make_png(192))
Path('icon-512.png').write_bytes(make_png(512))
print("Íconos creados.")
