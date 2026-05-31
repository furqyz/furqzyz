import json

def main():
    # Load quizData.js
    qd_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\assets\js\quizData.js"
    with open(qd_path, "r", encoding="utf-8") as f:
        qd_content = f.read().replace("const quizData = ", "").strip()
        if qd_content.endswith(";"): qd_content = qd_content[:-1]
    qd = json.loads(qd_content)
    
    # Map of page-column to types in PDF
    pdf_marks = {}
    for q in qd["questions"]:
        key = (q["page"], q["column"])
        if key not in pdf_marks:
            pdf_marks[key] = set()
        pdf_marks[key].add(q["type"])
        
    print(f"Total unique columns with marks in PDF: {len(pdf_marks)}")
    for key, types in sorted(pdf_marks.items()):
        print(f"  Page {key[0]} {key[1]}: marks={list(types)}")

    # Load cografyaQuestions.js
    cq_path = r"c:\Users\67ded\OneDrive\Masaüstü\Özethane\assets\js\cografyaQuestions.js"
    with open(cq_path, "r", encoding="utf-8") as f:
        cq_content = f.read().replace("const testQuestions = ", "").strip()
        if cq_content.endswith(";"): cq_content = cq_content[:-1]
    cq = json.loads(cq_content)
    
    print(f"\nTotal transcribed questions: {len(cq)}")
    # Print types in transcribed questions
    reds = [q for q in cq if q["type"] == "red"]
    turqs = [q for q in cq if q["type"] == "turquoise"]
    print(f"  Transcribed Red: {len(reds)}")
    print(f"  Transcribed Turquoise: {len(turqs)}")

if __name__ == "__main__":
    main()
