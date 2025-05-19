from openpyxl import Workbook

def write_to_excel(items):
    wb = Workbook()
    ws = wb.active
    ws.append(list(items[0].keys()))
    for item in items:
        ws.append(list(item.values()))

    wb.save("parser/wildberries.xlsx")
    