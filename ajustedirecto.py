import os
import wget

def create_report(desdedatacontrato, atedatacontrato, tipo, distrito):
    # Create the URL
    url = f"https://www.base.gov.pt/Base4/pt/resultados/?type=csv_contratos&tipo={tipo}&tipocontrato=0&desdedatacontrato={desdedatacontrato}&atedatacontrato={atedatacontrato}&pais=187&distrito={distrito}&concelho=0&sort(-publicationDate)"
    
    # Create the report filename
    report_num = len(os.listdir("reports")) + 1
    report_filename = f"{report_num}_{desdedatacontrato}"
    
    # Download the report
    wget.download(url, f"reports/{report_filename}")

def list_reports():
    reports = os.listdir("reports")
    for i, report in enumerate(reports):
        print(f"{i + 1}. {report}")
        
    remove_choice = input("Enter the number of the report you want to remove (or press Enter to cancel): ")
    if remove_choice:
        try:
            report_index = int(remove_choice) - 1
            os.remove(f"reports/{reports[report_index]}")
            print(f"Report {reports[report_index]} removed.")
        except (IndexError, ValueError):
            print("Invalid choice.")

# Main loop
if not os.path.exists("reports"):
    os.makedirs("reports")
    
while True:
    print("1. Create Report")
    print("2. Reports")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        desdedatacontrato = input("Enter the start date (YYYY-MM-DD): ")
        atedatacontrato = input("Enter the end date (YYYY-MM-DD): ")
        tipo = input("Enter the contract type ID: ")
        distrito = input("Enter the district ID: ")
        create_report(desdedatacontrato, atedatacontrato, tipo, distrito)
    elif choice == "2":
        list_reports()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
