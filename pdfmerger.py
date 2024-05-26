import PyPDF2

def merge_pdfs(pdf_list, output):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        pdf_merger.append(pdf)

    with open(output, 'wb') as f_out:
        pdf_merger.write(f_out)

if __name__ == "__main__":
    pdf_files = []  # List of PDF files to merge
    n=int(input("Enter the number of pdf you want to merge : "))
    for i in range(n):
        file=input(f"Enter the Pdf number {i+1} : ")
        newfile=file+".pdf"
        pdf_files.append(newfile)
        
    output_file = input("Enter the Merged Pdf name : ")+'.pdf' # Output file name

    merge_pdfs(pdf_files, output_file)
    print(f'Merged {len(pdf_files)} PDFs into {output_file}')
