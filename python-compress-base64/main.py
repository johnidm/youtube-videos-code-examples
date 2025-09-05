
import base64
import zlib

def decompress_base64(compressed_base64_string):
    """
    Decodes a compressed base64 string, decompresses the data, and returns the
    original data.
    """
    # Decode the base64 string to get the compressed binary data
    compressed_data = base64.b64decode(compressed_base64_string)

    # Decompress the binary data
    decoded_data = zlib.decompress(compressed_data)

    decompressed_base64_string = base64.b64encode(decoded_data).decode('utf-8')

    return decompressed_base64_string

def compress_base64(input_base64_string):
    """
    Decodes a base64 string, compresses the data, and returns the compressed data
    encoded in base64.
    """
    # Decode the base64 string to get the original binary data
    decoded_data = base64.b64decode(input_base64_string)

    # Compress the binary data
    compressed_data = zlib.compress(decoded_data)

    # Encode the compressed data back to base64
    compressed_base64_string = base64.b64encode(compressed_data)
    return compressed_base64_string


# A long string to get a meaningful compression example.
with open('car.png', 'rb') as f:
    original_base64 = base64.b64encode(f.read()).decode('utf-8')

# Compress the base64 string
compressed_base64 = compress_base64(original_base64)

# Decompress the compressed base64 string
decompressed_base64 = decompress_base64(compressed_base64)


with open('index.html', 'w') as f:
    f.write(f'''
        <html><body><h1>Car Image</h1>

        <img src="data:image/png;base64,{original_base64}" alt="Car Image">
        <hr>
        <img src="data:image/png;base64,{decompressed_base64}" alt="Compressed Car Image">

        </body></html>
    ''')


# Print the results
original_size = len(original_base64)
compressed_size = len(compressed_base64)


print(f"Original base64 string length: {original_size}")
print(f"Compressed base64 string length: {compressed_size}")
print(f"Decompressed base64 string length: {len(decompressed_base64)}")
print(f"Compression ratio: {original_size / compressed_size:.2f}x")

# Verify that the original and decompressed base64 strings are identical
assert original_base64 == decompressed_base64
print("Verification successful: The decompressed image is identical to the original.")
