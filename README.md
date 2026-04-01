# Local PDF Merger 📄🔗

A fast, lightweight Python-based CLI (Command Line Interface) tool to merge multiple PDF files locally on your machine. It requires no internet connection, ensuring your document privacy remains completely secure.

## Features
- **Extremely fast and lightweight.**
- **100% Offline:** Perfectly safe for sensitive and confidential documents.
- **Smart Sorting:** Automatically sorts files alphabetically or numerically before merging.
- **Safe Error Handling:** Skips corrupted PDF files gracefully without crashing the entire process.

## Prerequisites
Ensure you have Python 3.7 or newer installed on your system.

## Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/kirarutami/pdf-merge](https://github.com/kirarutami/pdf-merge)
   cd Local-PDF-Merger

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

## Usage
You can place this script in the same directory as your PDF files, or run it from anywhere via your terminal:

1. Basic Usage (Current Directory)
    Merges all PDFs in the current folder into a default merged_output.pdf file.
    ```bash
    python pdf_merger.py

2. Advanced Usage (Specific Directory and Output Name)
    Specify the target folder containing your PDFs and your desired output filename.
    ```bash
    python pdf_merger.py -d "C:\Path\To\Your\PDF\Folder" -o "Monthly_Report.pdf"

