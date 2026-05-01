// ── Dark mode toggle ──────────────────────────────────────────────────────
document.getElementById('darkToggle').addEventListener('click', () => {
    document.documentElement.classList.toggle('dark');
    localStorage.setItem('dark-mode', document.documentElement.classList.contains('dark'));
});

// ── State ─────────────────────────────────────────────────────────────────
let currentIndex = 0, score = 0, skipped = 0, answered = false;
const shuffled = [...testQuestions].sort(() => Math.random() - 0.5);
const total = shuffled.length;

// ── DOM refs ──────────────────────────────────────────────────────────────
const counterEl    = document.getElementById('testCounter');
const progressBar  = document.getElementById('progressBar');
const questionEl   = document.getElementById('testQuestionText');
const optionsEl    = document.getElementById('testOptions');
const feedbackEl   = document.getElementById('testFeedback');
const nextBtn      = document.getElementById('nextQuestionBtn');
const skipBtn      = document.getElementById('skipBtn');
const scoreCounter = document.getElementById('scoreCounter');
const testCard     = document.getElementById('testCard');
const finishScreen = document.getElementById('finishScreen');

// ── Load question ─────────────────────────────────────────────────────────
function loadQuestion() {
    answered = false;
    const q = shuffled[currentIndex];
    counterEl.textContent = `Soru ${currentIndex + 1} / ${total}`;
    progressBar.style.width = `${(currentIndex / total) * 100}%`;
    questionEl.textContent = q.question;

    // reset feedback & next btn
    feedbackEl.innerHTML = '';
    feedbackEl.className = 'text-sm font-semibold opacity-0 transition-opacity duration-300 flex items-center gap-2';
    nextBtn.className = 'opacity-0 pointer-events-none flex items-center gap-2 bg-indigo-600 hover:bg-indigo-700 active:scale-95 text-white px-5 py-2.5 rounded-2xl font-bold transition-all duration-200 shadow-md shadow-indigo-200 dark:shadow-none';
    nextBtn.innerHTML = currentIndex === total - 1
        ? '<i class="fas fa-flag-checkered"></i> Testi Bitir'
        : 'Sonraki Soru <i class="fas fa-arrow-right"></i>';
    skipBtn.disabled = false;
    skipBtn.classList.remove('opacity-40');

    // build option buttons
    optionsEl.innerHTML = '';
    const keys = Object.keys(q.options).sort();
    keys.forEach(key => {
        const btn = document.createElement('button');
        btn.className = 'option-btn w-full text-left flex items-center gap-4 p-4 rounded-2xl border-2 border-slate-100 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 hover:border-indigo-300 dark:hover:border-indigo-500 hover:bg-indigo-50 dark:hover:bg-indigo-900/20 text-slate-700 dark:text-slate-200 font-medium';
        btn.dataset.key = key;
        btn.innerHTML = `<span class="w-9 h-9 shrink-0 flex items-center justify-center rounded-full bg-white dark:bg-slate-700 border border-slate-200 dark:border-slate-600 font-bold text-slate-500 dark:text-slate-300 text-sm">${key}</span><span>${q.options[key]}</span>`;
        btn.addEventListener('click', () => selectOption(key, q));
        optionsEl.appendChild(btn);
    });
}

// ── Select option ─────────────────────────────────────────────────────────
function selectOption(selected, q) {
    if (answered) return;
    answered = true;
    skipBtn.disabled = true;
    skipBtn.classList.add('opacity-40');

    const correct = q.answer;
    const isCorrect = selected === correct;
    if (isCorrect) score++;
    scoreCounter.textContent = `${score} ✓`;

    optionsEl.querySelectorAll('.option-btn').forEach(b => {
        b.disabled = true;
        const k = b.dataset.key;
        const circle = b.querySelector('span:first-child');
        const baseRemove = ['border-slate-100','dark:border-slate-700','bg-slate-50','dark:bg-slate-800','hover:border-indigo-300','dark:hover:border-indigo-500','hover:bg-indigo-50','dark:hover:bg-indigo-900/20'];
        if (k === correct) {
            b.classList.remove(...baseRemove);
            b.classList.add('border-emerald-400','bg-emerald-50','dark:bg-emerald-900/20','dark:border-emerald-500');
            circle.classList.add('bg-emerald-500','text-white','border-emerald-500');
            circle.classList.remove('bg-white','dark:bg-slate-700','border-slate-200','dark:border-slate-600','text-slate-500','dark:text-slate-300');
            if (isCorrect) b.classList.add('pop');
        } else if (k === selected) {
            b.classList.remove(...baseRemove);
            b.classList.add('border-rose-400','bg-rose-50','dark:bg-rose-900/20','dark:border-rose-500');
            circle.classList.add('bg-rose-500','text-white','border-rose-500');
            circle.classList.remove('bg-white','dark:bg-slate-700','border-slate-200','dark:border-slate-600','text-slate-500','dark:text-slate-300');
            b.classList.add('shake');
        } else {
            b.classList.add('opacity-40');
        }
    });

    feedbackEl.innerHTML = isCorrect
        ? '<i class="fas fa-check-circle text-emerald-500"></i><span class="text-emerald-600 dark:text-emerald-400">Doğru!</span>'
        : `<i class="fas fa-times-circle text-rose-500"></i><span class="text-rose-600 dark:text-rose-400">Cevabın yanlış; doğrusu <strong>${correct}) ${q.options[correct]}</strong> olmalıydı</span>`;
    feedbackEl.classList.remove('opacity-0');
    feedbackEl.classList.add('opacity-100');

    nextBtn.classList.remove('opacity-0','pointer-events-none');
    nextBtn.classList.add('opacity-100');
}

// ── Advance ───────────────────────────────────────────────────────────────
function advance() {
    if (currentIndex >= total - 1) { showFinish(); return; }
    currentIndex++;
    testCard.style.opacity = '0';
    testCard.style.transform = 'translateX(-8px)';
    setTimeout(() => {
        loadQuestion();
        testCard.style.transform = 'translateX(8px)';
        requestAnimationFrame(() => requestAnimationFrame(() => {
            testCard.style.opacity = '1';
            testCard.style.transform = 'translateX(0)';
        }));
    }, 160);
}

nextBtn.addEventListener('click', () => { if (answered) advance(); });

// Skip (doesn't count as wrong, just moves on)
skipBtn.addEventListener('click', () => {
    if (answered) return;
    skipped++;
    advance();
});

// ── Keyboard shortcuts ────────────────────────────────────────────────────
document.addEventListener('keydown', e => {
    const key = e.key.toUpperCase();
    if (!answered && ['A','B','C','D','E'].includes(key)) {
        const btn = optionsEl.querySelector(`[data-key="${key}"]`);
        if (btn) btn.click();
    } else if (answered && (e.key === 'Enter' || e.key === 'ArrowRight')) {
        advance();
    } else if (!answered && e.key === 'ArrowRight') {
        skipBtn.click();
    }
});

// ── Finish ────────────────────────────────────────────────────────────────
function showFinish() {
    testCard.classList.add('hidden');
    finishScreen.classList.remove('hidden');
    progressBar.style.width = '100%';
    const pct = Math.round((score / (total - skipped)) * 100) || 0;
    document.getElementById('finalScore').textContent =
        `${total} sorudan ${score} doğru · ${skipped} atlama · Başarı: %${pct}`;
    const rating = pct >= 85 ? '🏆 Mükemmel!' : pct >= 70 ? '🎯 Çok İyi!' : pct >= 50 ? '📈 Gelişiyor!' : '💪 Daha çok çalış!';
    document.getElementById('finalRating').textContent = rating;
    document.getElementById('finishEmoji').textContent = pct >= 70 ? '🎉' : '📚';
}

function restartTest() {
    currentIndex = 0; score = 0; skipped = 0;
    shuffled.sort(() => Math.random() - 0.5);
    scoreCounter.textContent = '0 ✓';
    finishScreen.classList.add('hidden');
    testCard.classList.remove('hidden');
    testCard.style.opacity = '1';
    testCard.style.transform = '';
    loadQuestion();
}

loadQuestion();
