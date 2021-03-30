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

print("++++++++++++++++++++++++BUILDING++++++++++++++++++++++++")
for s in purged_lines:
    if "error:" in s:
        print("\033[31merror:\033[0m".join(s.split("error:")))
    else:
        print(s)

print("------------------------FINISHED------------------------")
