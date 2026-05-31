import json

def main():
    log_path = r"C:\Users\67ded\.gemini\antigravity\brain\0f0884f0-da21-4d63-a6fb-04db700574dd\.system_generated\logs\transcript.jsonl"
    
    with open(log_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if "cografyaQuestions.js" in line:
                try:
                    obj = json.loads(line)
                    print(f"Line {idx+1}: Type={obj.get('type')}, Source={obj.get('source')}")
                    # Let's print a small snippet of content
                    content = obj.get("content", "")
                    if content:
                        print(f"  Content snippet: {content[:100]}...")
                    # Print tool calls if any
                    tool_calls = obj.get("tool_calls", [])
                    if tool_calls:
                        for tc in tool_calls:
                            print(f"  Tool: {tc.get('name')}")
                            args = tc.get("arguments", {})
                            if "TargetFile" in args:
                                print(f"    TargetFile: {args['TargetFile']}")
                except Exception as e:
                    print(f"Error parsing line {idx+1}: {e}")

if __name__ == "__main__":
    main()
