import os
import gzip
import zipfile

def analyze_compressed_file_header(file_path):
    if not os.path.isfile(file_path):
        print("Error: File not found.")
        return

    if file_path.endswith('.gz'):
        analyze_gzip_header(file_path)
    elif file_path.endswith('.zip'):
        analyze_zip_header(file_path)
    else:
        print("Error: Unsupported compression format.")

def analyze_gzip_header(file_path):
    with gzip.open(file_path, 'rb') as f:
        header = f.read(64)  # Read the first 64 bytes of the compressed file

    print("Header Information:")
    print("--------------------")
    print(f"File Path: {file_path}")
    print(f"Uncompressed File Size: {os.path.getsize(file_path)} bytes")

    print("\nFirst 64 bytes (in hexadecimal):")
    print(' '.join(f"{byte:02X}" for byte in header))

    print("\nFirst 64 bytes (in ASCII):")
    print(''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in header))

def analyze_zip_header(file_path):
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        first_file = zip_file.namelist()[0]  # Get the first file in the zip archive
        with zip_file.open(first_file) as f:
            header = f.read(64)  # Read the first 64 bytes of the first file in the zip archive

    print("Header Information:")
    print("--------------------")
    print(f"File Path: {file_path}")
    print(f"Number of Files in Zip: {len(zip_file.namelist())}")

    print("\nFirst 64 bytes (in hexadecimal):")
    print(' '.join(f"{byte:02X}" for byte in header))

    print("\nFirst 64 bytes (in ASCII):")
    print(''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in header))

if __name__ == "__main__":
    file_path = input("Enter the path to the compressed file: ")
    analyze_compressed_file_header(file_path)
