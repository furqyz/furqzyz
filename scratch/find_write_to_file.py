import json

def main():
    log_path = r"C:\Users\67ded\.gemini\antigravity\brain\0f0884f0-da21-4d63-a6fb-04db700574dd\.system_generated\logs\transcript.jsonl"
    with open(log_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if "cografyaQuestions.js" in line:
                try:
                    obj = json.loads(line)
                    tool_calls = obj.get("tool_calls", [])
                    for tc in tool_calls:
                        args = tc.get("arguments", {})
                        target = args.get("TargetFile", "")
                        if target and "cografyaQuestions.js" in target:
                            code = args.get("CodeContent", "")
                            print(f"Match on Line {idx+1}: Tool={tc.get('name')}, TargetFile={target}, CodeContent length={len(code)}")
                            if len(code) > 0:
                                print(f"  Code snippet:\n{code[:300]}...\n")
                except Exception as e:
                    pass

if __name__ == "__main__":
    main()
