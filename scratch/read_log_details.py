import json

def main():
    log_path = r"C:\Users\67ded\.gemini\antigravity\brain\0f0884f0-da21-4d63-a6fb-04db700574dd\.system_generated\logs\transcript.jsonl"
    with open(log_path, "r", encoding="utf-8") as f:
        lines = list(f)
    
    # Let's inspect line 3443 (index 3442) and print its details
    line = lines[3442]
    obj = json.loads(line)
    tool_calls = obj.get("tool_calls", [])
    if tool_calls:
        tc = tool_calls[0]
        print(f"Tool name: {tc.get('name')}")
        args = tc.get("arguments", {})
        print(f"TargetFile: {args.get('TargetFile')}")
        code = args.get("CodeContent", "")
        print(f"CodeContent (length={len(code)}):\n{code[:800]}")
    else:
        print("No tool calls found on Line 3443.")

if __name__ == "__main__":
    main()
