import os
import time
import wget
import csv
import re

def create_report(desdedatacontrato, atedatacontrato, tipo, distrito):
    # Create the URL
    url = f"https://www.base.gov.pt/Base4/pt/resultados/?type=csv_contratos&tipo={tipo}&tipocontrato=0&desdedatacontrato={desdedatacontrato}&atedatacontrato={atedatacontrato}&pais=187&distrito={distrito}&concelho=0&sort(-publicationDate)"

    # Create the report filename
    report_num = len(os.listdir("reports")) + 1
    report_filename = f"{report_num}_{desdedatacontrato}"

    # Download the report
    bar_char = wget.bar_adaptive
    run_bar(total_time=20)
    print("getting done...running api...")
    wget.download(url, f"reports/{report_filename}",bar=bar_char)

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS, etc.
        os.system('clear')

def run_bar(total_time):
    for i in range(total_time):
        print("#", end="", flush=True)
        time.sleep(1)
    print("\n")


def print_districts_table():
    districts = [
        "1:Outros", "2:Aveiro", "3:Beja", "4:Braga", "5:Bragança",
        "6:Castelo Branco", "7:Coimbra", "8:Évora", "9:Faro", "10:Guarda",
        "11:Leiria", "12:Lisboa", "13:Portalegre", "14:Porto", "15:Santarém",
        "16:Setúbal", "17:Viana do Castelo", "18:Vila Real", "19:Viseu",
        "20:Região Autónoma do Açores", "21:Região Autónoma da Madeira",
        "22:Portugal Continental", "23:Distrito não determinado",
        "24:Consulados Situados no estrangeiro"
    ]

    row_format = "{:<15}" * 3
    print(row_format.format("District 1", "District 2", "District 3"))
    for i in range(0, len(districts), 3):
        district_group = districts[i:i+3]
        formatted_districts = [f"{index + 1}: {district}" for index, district in enumerate(district_group)]
        print(row_format.format(*formatted_districts))

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
def display_analytics():
    report_files = os.listdir("reports")
    if len(report_files) == 0:
        print("No reports found.")
        return
    contracts = []
    for file in report_files:
        with open(f"reports/{file}", "r", encoding="utf-8" as f:
            reader = csv.DictReader(f, delimiter=';')
            column_names = reader.fieldnames
            #print("Column names in the CSV file:")
            #print(column_names)
            for now in reader:
                contracts.append(row)

    valid_contracts = [contract for contract in contracts if 'CPV Valor' in contract]
    if len(valid_contracts) == 0:
        print("No contracts with 'CPV Valor' found.")
        return
    sorted_contracts = sorted(valid_contracts, key=lambda x: float(re.sub(r'\D', '', x['CPV Valor'])), reverse=True)
    top_10_contracts = sorted_contracts[:10]
    print("Top 10 Contracts by CPV Valor:")
    for contracts in top_10_contracts:
        contract_description = contract['CPV']
        cpv_valor = contract['CPV Valor']
        print(f"Contract Description: {contract_description}, CPV VAlor: {cpv_valor}")    
# Main loop
clear_screen()  # call this function to clear the screen
if not os.path.exists("reports"):
    os.makedirs("reports")
print("A J U S T E D I R E C T O")
print(" /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ ")
print("( A )( J )( U )( S )( T )( E )( D )( I )( R )( E )( C )( T )( O )\n")
while True:
    print("1. Create Report")
    print("2. Reports")
    print("3. Analytics")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        desdedatacontrato = input("Enter the start date (YYYY-MM-DD): ")
        atedatacontrato = input("Enter the end date (YYYY-MM-DD): ")
        print("Available contract types:")
        print("1: Ajuste Directo (Regime Geral)")
        print("18: Ajuste Direto Regime Geral ao abrigo do artigo 7º da Lei n.º 30/2021, de 21.05")
        print("20: Ajuste direto simplificado")
        print("21: Ajuste direto simplificado ao abrigo da Lei n.º 30/2021, de 21.05")
        tipo = input("Enter the contract type ID: ")
        print("Available districts:")
        print_districts_table()
        distrito = input("Enter the district ID: ")
        create_report(desdedatacontrato, atedatacontrato, tipo, distrito)
    elif choice == "2":
        list_reports()
        clear_screen()  # call this function to clear the screen
    elif choice == "3":
        display_analytics()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
