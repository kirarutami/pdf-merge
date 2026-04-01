import argparse
import logging
import sys
from pathlib import Path
from pypdf import PdfWriter

# Configure Logging for professional terminal output (instead of just using print)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def merge_pdfs(input_dir: str, output_file: str) -> None:
    """
    Merges all PDF files in the specified directory into a single file.

    Args:
        input_dir (str): Path to the folder containing the PDF files.
        output_file (str): Filename or path for the merged PDF output.
    """
    target_dir = Path(input_dir)
    output_path = Path(output_file)

    # Validate if the directory exists
    if not target_dir.is_dir():
        logging.error(f"Directory not found: {target_dir.absolute()}")
        sys.exit(1)

    # Use pathlib to find and sort PDF files (more modern than os/glob)
    pdf_files = sorted(target_dir.glob("*.pdf"))

    # Exclude the output file from being processed if it already exists in the same folder
    pdf_files = [f for f in pdf_files if f.resolve() != output_path.resolve()]

    if not pdf_files:
        logging.warning(f"No PDF files found in: {target_dir.absolute()}")
        return

    logging.info(f"Found {len(pdf_files)} PDF file(s). Starting the merge process...")

    writer = PdfWriter()
    successful_merges = 0

    for pdf in pdf_files:
        try:
            writer.append(pdf)
            logging.info(f"Added: {pdf.name}")
            successful_merges += 1
        except Exception as e:
            logging.error(f"Failed to add {pdf.name} - Error: {e}")

    # Save the final output if any files were successfully merged
    if successful_merges > 0:
        try:
            # Ensure the target directory for the output file exists
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, "wb") as out_file:
                writer.write(out_file)
            logging.info(f"SUCCESS! {successful_merges} PDF(s) merged into: {output_path.absolute()}")
        except Exception as e:
            logging.error(f"Failed to save the output file: {e}")
    else:
        logging.warning("No pages were successfully merged.")

if __name__ == "__main__":
    # Setup Argparse so the script accepts arguments like a real CLI tool
    parser = argparse.ArgumentParser(
        description="A simple and fast tool to merge multiple PDF files.",
        epilog="Example usage: python pdf_merger.py -d ./documents -o final_report.pdf"
    )
    
    parser.add_argument(
        "-d", "--dir", 
        type=str, 
        default=".", 
        help="Directory where the PDF files are located (default: current directory)"
    )
    parser.add_argument(
        "-o", "--output", 
        type=str, 
        default="merged_output.pdf", 
        help="Name of the output file (default: merged_output.pdf)"
    )

    args = parser.parse_args()

    # Execute the main function
    merge_pdfs(input_dir=args.dir, output_file=args.output)