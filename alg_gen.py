'''
INSTRUCTIONS
1. Create a file with the following code
2. Put the file you want to convert into the same folder as it, and rename it to "file.py"
3. Add a "#F" comment to any lines in the code which have a function call that doesn't assign anything (so no =),
as the program cannot handle these convincingly
4. Run the converter file
'''

import re

python_file = 'biggest.py'
work_file = None

basic_conversion_rules = {"for": "for", "=": "to", "if": "if", "==": "equals", "while": "while", "until": "until", "import": "import", "class": "define class", "def": "define function", "else:": "else:", "elif": "elseif", "except:": "except:", "try:": "try:", "pass": "pass", "in": "in"}
prefix_conversion_rules = {"=": "set ", "#F": "call "}
advanced_conversion_rules = {"print": "print", "return": "return", "input": "input"}

def f2list(to_list):
    return to_list.readlines()

def l2pseudo(to_pseudo):
    for line in to_pseudo:
        line_index = to_pseudo.index(line)
        line = str(line)
        line = re.split(r'(\s+)', line)  
        line.insert(0,f"Step {line_index+ 1}: ")
        for key, value in prefix_conversion_rules.items():
            if key in line:
                if not str(line[1]) == '':
                    line[1] = value + line[1]
                else:
                    line[2] = value + line[2]
        for key, value in basic_conversion_rules.items():
            for word in line:
                if key == str(word):
                    line[line.index(word)] = value
        for key, value in advanced_conversion_rules.items():
            for word in line:
                line[line.index(word)] = word.replace(key, value)
        for key, value in prefix_conversion_rules.items():
            for word in line:
                if word == key:
                    del line[line.index(word)]
        to_pseudo[line_index]= "".join(line)
    return(to_pseudo)

def p2file(to_file):
    file = open(python_file + '_algorithm.txt', 'w', encoding="utf8")
    for line in to_file:
        print(line, file=file)

def main():
    main_file = open(python_file, 'r+') 
    work_file = f2list(main_file)
    work_file.remove('\n')
    work_file.insert(0,"Start\n")
    work_file.append("Stop")
    work_file = l2pseudo(work_file)
    p2file(work_file)
    

main()
