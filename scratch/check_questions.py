import json
import re

def main():
    js_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\assets\js\cografyaQuestions.js"
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Strip JS parts to get JSON
    json_str = content.replace("const testQuestions = ", "")
    # Remove trailing semicolon if any
    json_str = json_str.strip()
    if json_str.endswith(";"):
        json_str = json_str[:-1]
        
    db = json.loads(json_str)
    print(f"Total questions in database: {len(db)}")
    
    reds = [q for q in db if q["type"] == "red"]
    turqs = [q for q in db if q["type"] == "turquoise"]
    print(f"Red type: {len(reds)}")
    print(f"Turquoise type: {len(turqs)}")
    
    for i, q in enumerate(db):
        first_line = q["question"].splitlines()[0] if q["question"] else ""
        print(f"  {i+1:2d}. [{q['type']}] {first_line[:50]}...")

if __name__ == "__main__":
    main()
