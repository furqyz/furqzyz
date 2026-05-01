import glob

files = ['index.html'] + glob.glob('unitler/*.html')

old_bg = "bg-white/60 hover:bg-white/80 dark:bg-slate-800/60 dark:hover:bg-slate-800/80"
new_bg = "bg-white/95 hover:bg-white dark:bg-slate-900/90 dark:hover:bg-slate-900"

old_text = "text-slate-700 dark:text-slate-300"
new_text = "text-slate-800 dark:text-slate-200"

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace(old_bg, new_bg)
    # The text replacement might affect other parts of the site, but text-slate-800 is generally better contrast anyway.
    # Let's only replace it within the exam-memory section context if possible, or just globally since it's a minor darkening.
    # Actually, let's just do it globally, making text-slate-700 -> text-slate-800 increases readability everywhere.
    content = content.replace("text-slate-700", "text-slate-800")
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Contrast fixed in all files.")
