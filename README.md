# A-solution-to-the-zip-bomb-problem
Python script pulls the header information of the compressed file and through it we check whether the file is a bomb or not
## Analyze Compressed File Header

This Python script analyzes the header of compressed files, supporting both gzip (.gz) and zip (.zip) formats. It provides information about the file path, uncompressed file size, number of files in case of zip archives, and displays the first 64 bytes of the file in hexadecimal and ASCII format.

### Script Components:

#### 1. `analyze_compressed_file_header(file_path)`

This function is the entry point of the script. It takes a file path as input and determines the type of compression (gzip or zip) based on the file extension. It then calls the respective analysis function.

#### 2. `analyze_gzip_header(file_path)`

This function analyzes the header of a gzip compressed file. It reads the first 64 bytes of the file and displays information such as the file path, uncompressed file size, and the first 64 bytes in both hexadecimal and ASCII format.

#### 3. `analyze_zip_header(file_path)`

This function analyzes the header of a zip compressed file. It extracts the first file in the zip archive, reads the first 64 bytes of that file, and displays similar information as the `analyze_gzip_header` function.

### How to Use:

1. Run the script.
2. Enter the path to the compressed file when prompted.
3. The script will analyze the header of the file and display the information.

### Example Usage:

```python
python analyze_compressed_file_header.py


Feel free to adjust the explanation according to your preferences or add any additional information you think might be useful.
