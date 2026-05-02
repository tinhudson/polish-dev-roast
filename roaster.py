import random
from typing import Dict

class PolishDevRoaster:
    def __init__(self):
        self.templates = [
            "Kurwa {dev}, serio? {issue}",
            "No i po co mi to pokazujesz {dev}? {issue}",
            "{dev}... ja pierdolę... {issue}",
            "Jakoś tak się nie dało {better}? {issue}",
            "W 2026 roku nadal piszesz {bad_thing}? Szacun.",
        ]
        
        self.insults = {
            "naming": ["zmienne typu `x`, `data`, `temp` jak w 2008"],
            "architecture": ["to nie jest architektura, to jest katastrofa urbanistyczna"],
            "performance": ["to ma O(n²) i się dziwi że na produkcji pada"],
            "comments": ["komentarze po polsku z błędami — mistrzostwo"],
        }

    def roast(self, code: str, dev_name: str = "kolego") -> str:
        issues = []
        
        if any(var in code.lower() for var in ['x ', 'temp', 'data1', 'result']):
            issues.append(random.choice(self.insults["naming"]))
        
        if len(code.split('\n')) > 80 and 'def ' in code:
            issues.append("masz jedną funkcję na 120 linii? Brawo maestro")
        
        if 'except:' in code or 'except Exception' in code:
            issues.append("except Exception jak prawdziwy wojownik")
            
        if 'print(' in code and 'def main' in code:
            issues.append("printy w produkcji? Szacun za odwagę")

        roast_line = random.choice(self.templates)
        issue = random.choice(issues) if issues else "cały kod jest jednym wielkim czerwonym flagiem"
        
        return roast_line.format(dev=dev_name, issue=issue, bad_thing="takie rzeczy")


# CLI
if __name__ == "__main__":
    import sys
    roaster = PolishDevRoaster()
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            code = f.read()
        print(roaster.roast(code, "seniorze"))
    else:
        print(roaster.roast("def x(y): return y*2", "Janusz"))
