import json

def main():
    log_path = r"C:\Users\67ded\.gemini\antigravity\brain\0f0884f0-da21-4d63-a6fb-04db700574dd\.system_generated\logs\transcript.jsonl"
    with open(log_path, "r", encoding="utf-8") as f:
        lines = list(f)
    
    # Let's inspect line 3443 (index 3442) and print its details
    line = lines[3442]
    obj = json.loads(line)
    # Print keys and values except very long content
    for k, v in obj.items():
        if k == "content":
            print(f"content: {v[:200]}...")
        elif k == "tool_calls":
            print(f"tool_calls: {json.dumps(v, indent=2)[:500]}...")
        else:
            print(f"{k}: {v}")

if __name__ == "__main__":
    main()
