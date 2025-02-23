bug_reports = ["Ошибка 1 — High","Ошибка 2 — Low", "Ошибка 3 — Medium", "Ошибка 4 — High","Ошибка 5 — Low"]
bug_reports.append("Ошибка 6 - Medium")

for bug in bug_reports:
    if "Low" in bug:
        bug_reports.remove(bug)
        break

def get_priority(bug):
    if "High" in bug:
        return 1
    elif "Medium" in bug:
        return 2
    elif "Low" in bug:
        return 3
    else:
        return 4

bug_reports.sort(key=get_priority)
print(bug_reports)