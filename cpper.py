lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break
purged_lines = []
purging_lines = True
last_line = ""
for s in lines:
    if not purging_lines:
        purged_lines.append(s)
    if "error:" in s and purging_lines:
        purging_lines = False
        purged_lines.append(last_line)
        purged_lines.append(s)
    if "note:" in s and not purging_lines:
        purging_lines = True
        purged_lines = purged_lines[:-1]
    last_line = s
for s in purged_lines:
    print(s)