import json

def main():
    log_path = r"C:\Users\67ded\.gemini\antigravity\brain\0f0884f0-da21-4d63-a6fb-04db700574dd\.system_generated\logs\transcript.jsonl"
    
    with open(log_path, "r", encoding="utf-8") as f:
        lines = list(f)
        
    print(f"Total lines in transcript: {len(lines)}")
    
    # Read around line 3443 (0-indexed: 3442)
    start = max(0, 3438)
    end = min(len(lines), 3446)
    
    for idx in range(start, end):
        line = lines[idx]
        obj = json.loads(line)
        print(f"\n--- Line {idx+1} ({obj.get('type')}, {obj.get('source')}) ---")
        tool_calls = obj.get("tool_calls", [])
        if tool_calls:
            for tc in tool_calls:
                print(f"Tool name: {tc.get('name')}")
                args = tc.get("arguments", {})
                if "TargetFile" in args:
                    print(f"  TargetFile: {args['TargetFile']}")
                # Print arguments summary
                for k, v in args.items():
                    if k != "CodeContent" and k != "ReplacementContent":
                        print(f"  {k}: {v}")
                    else:
                        print(f"  {k} (length={len(v)})")

if __name__ == "__main__":
    main()
