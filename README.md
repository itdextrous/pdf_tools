# PDF Tools 📝  
A simple command-line tool for working with PDFs.  
This tool provides two primary functionalities:  
- **Generating PDF files** with provided text or dummy text 
- **Highlighting specified text** in PDF files  

## 🚀 Installation  
To install the tool, run the following command in a Python environment. Ensure that the environment where you plan to use this tool remains the same as the one where it is installed.  

Navigate to the project's root directory (where `pyproject.toml` is located) and execute:  
```sh
pip install .
```

## 📌 Usage  
Once installed, the tool can be accessed via the command line using `pdf_tools`.  

### ✨ Generating PDFs  
To generate a PDF file, use the following command:  
```sh
pdf_tools generate <output_directory> --content <content_value (optional)> --pages <pages_value (optional)> --name <file_name (optional)>
```  
- **Required Argument:**  
  - `output_directory` – The directory where the generated PDF will be saved.  
- **Optional Arguments:**  
  - `--content` – If not provided, the PDF will contain random lorem ipsum text.  
  - `--pages` – If omitted, a single-page PDF will be created. If specified, the PDF will contain the given number of pages.  
  - `--name` – Specifies the output file name.  
- **Note:**  
  - If `--content` is provided, the `--pages` parameter will be ignored, and the number of pages will be determined by the content length.  

### 🔍 Highlighting Text in PDFs  
To highlight text in a PDF file using a CSV input, run:  
```sh
pdf_tools highlight <csv_file_location> <output_directory>
```  
- **Required Arguments:**  
  - `csv_file_location` – The path to the CSV file containing the highlight instructions.  
  - `output_directory` – The directory where the modified PDF will be saved.  
- **CSV Format:**  
  The CSV file should contain the following columns:  
  - `file` – Absolute path to the PDF file.  
  - `word` – The text to be highlighted.  
  - `page` – The page number (optional; leave empty if not needed).  
  - `exact` – Boolean (`true` or `false`); if `true`, the match must be exact.  

#### 📝 Sample CSV File:  
```
file,word,page,exact
/path/to/pdf1.pdf,word1,2,false
/path/to/pdf2.pdf,word2,,true
```
- If the `page` column is empty, the entire document will be searched for the word.  
- The highlighted text will appear in a **light yellow** color.  

