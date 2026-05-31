// ── State ─────────────────────────────────────────────────────────────────
let shuffledQuestions = [];
let currentIndex = 0;
let answered = false;

// Stats for current session
let correctAnswers = 0;
let wrongAnswers = 0;
let skippedAnswers = 0;

// ── DOM refs ──────────────────────────────────────────────────────────────
const testCounter = document.getElementById('testCounter');
const progressBar = document.getElementById('progressBar');
const scoreCounter = document.getElementById('scoreCounter');

const quizContainer = document.getElementById('quiz-container');
const questionIndexBadge = document.getElementById('question-index-badge');
const questionTypeBadge = document.getElementById('question-type-badge');

const questionText = document.getElementById('question-text');
const mapContainer = document.getElementById('map-container');
const questionMap = document.getElementById('question-map');
const testOptions = document.getElementById('test-options');

const testFeedback = document.getElementById('test-feedback');
const skipBtn = document.getElementById('skip-btn');
const nextBtn = document.getElementById('next-question-btn');

const solutionPanel = document.getElementById('solution-panel');
const solutionBadge = document.getElementById('solution-badge');
const explanationText = document.getElementById('explanation-text');

const finishScreen = document.getElementById('finish-screen');
const finishEmoji = document.getElementById('finish-emoji');
const finalScore = document.getElementById('final-score');
const finalRating = document.getElementById('final-rating');

// ── Init Quiz ─────────────────────────────────────────────────────────────
function initQuiz() {
    shuffledQuestions = [...testQuestions].sort(() => Math.random() - 0.5);
    
    currentIndex = 0;
    correctAnswers = 0;
    wrongAnswers = 0;
    skippedAnswers = 0;
    
    updateStatsUI();
    
    if (finishScreen) finishScreen.classList.add('hidden');
    if (quizContainer) quizContainer.classList.remove('hidden');
    
    loadQuestion();
}

// ── Update Stats ──────────────────────────────────────────────────────────
function updateStatsUI() {
    if (scoreCounter) {
        scoreCounter.textContent = `${correctAnswers} ✓`;
    }
    if (testCounter && shuffledQuestions.length > 0) {
        testCounter.textContent = `Soru ${currentIndex + 1} / ${shuffledQuestions.length}`;
    }
    if (progressBar && shuffledQuestions.length > 0) {
        progressBar.style.width = `${(currentIndex / shuffledQuestions.length) * 100}%`;
    }
}

// ── Load Question ─────────────────────────────────────────────────────────
function loadQuestion() {
    answered = false;
    const q = shuffledQuestions[currentIndex];
    
    // index and progress update
    if (questionIndexBadge) questionIndexBadge.textContent = `Soru ${currentIndex + 1} / ${shuffledQuestions.length}`;
    
    // type badge
    if (questionTypeBadge) {
        if (q.type === 'red') {
            questionTypeBadge.textContent = "🔴 YANLIŞ YAPILAN";
            questionTypeBadge.className = "px-3 py-1 bg-rose-50 dark:bg-rose-950/40 text-rose-600 dark:text-rose-400 text-xs font-bold rounded-md uppercase tracking-wider";
        } else {
            questionTypeBadge.textContent = "✨ BEĞENİLEN NOT";
            questionTypeBadge.className = "px-3 py-1 bg-teal-50 dark:bg-teal-950/40 text-teal-600 dark:text-teal-400 text-xs font-bold rounded-md uppercase tracking-wider";
        }
    }
    
    // question text
    if (questionText) {
        questionText.innerHTML = q.question.replace(/\n/g, '<br>');
    }
    
    // dynamic map check
    if (q.image) {
        if (questionMap) questionMap.src = '../' + q.image;
        if (mapContainer) mapContainer.classList.remove('hidden');
    } else {
        if (mapContainer) mapContainer.classList.add('hidden');
    }
    
    // reset panel & buttons
    if (solutionPanel) solutionPanel.classList.add('hidden');
    if (testFeedback) {
        testFeedback.innerHTML = '';
        testFeedback.className = 'text-sm font-semibold opacity-0 transition-opacity duration-300 flex items-center gap-2';
    }
    
    if (nextBtn) {
        nextBtn.className = 'flex-1 sm:flex-none opacity-0 pointer-events-none flex items-center justify-center gap-2 bg-emerald-600 hover:bg-emerald-700 active:scale-95 text-white px-5 py-2.5 rounded-xl font-bold transition-all duration-200 shadow-md shadow-emerald-200 dark:shadow-none text-xs';
        nextBtn.innerHTML = currentIndex === shuffledQuestions.length - 1
            ? '<i class="fas fa-flag-checkered"></i> Testi Bitir'
            : 'Sonraki Soru <i class="fas fa-arrow-right"></i>';
    }
    
    if (skipBtn) {
        skipBtn.disabled = false;
        skipBtn.classList.remove('opacity-40');
    }
    
    // build options
    if (testOptions) {
        testOptions.innerHTML = '';
        const keys = Object.keys(q.options).sort();
        keys.forEach(key => {
            const btn = document.createElement('button');
            btn.className = 'option-btn w-full text-left flex items-start gap-4 p-4 rounded-2xl border-2 border-slate-100 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 hover:border-emerald-300 dark:hover:border-emerald-500 hover:bg-emerald-50/30 dark:hover:bg-emerald-950/10 text-slate-700 dark:text-slate-200 font-medium';
            btn.dataset.key = key;
            btn.innerHTML = `<span class="w-9 h-9 shrink-0 flex items-center justify-center rounded-full bg-white dark:bg-slate-700 border border-slate-200 dark:border-slate-600 font-bold text-slate-500 dark:text-slate-300 text-sm">${key}</span><span class="pt-1.5 leading-normal">${q.options[key]}</span>`;
            btn.addEventListener('click', () => selectOption(key, q));
            testOptions.appendChild(btn);
        });
    }
}

// ── Select Option ─────────────────────────────────────────────────────────
function selectOption(selected, q) {
    if (answered) return;
    answered = true;
    
    if (skipBtn) {
        skipBtn.disabled = true;
        skipBtn.classList.add('opacity-40');
    }
    
    const correct = q.answer;
    const isCorrect = selected === correct;
    
    if (isCorrect) {
        correctAnswers++;
    } else {
        wrongAnswers++;
    }
    updateStatsUI();
    
    // Style Option Buttons
    if (testOptions) {
        testOptions.querySelectorAll('.option-btn').forEach(btn => {
            btn.disabled = true;
            const k = btn.dataset.key;
            const circle = btn.querySelector('span:first-child');
            const baseRemove = [
                'border-slate-100', 'dark:border-slate-700', 'bg-slate-50', 'dark:bg-slate-800',
                'hover:border-emerald-300', 'dark:hover:border-emerald-500', 'hover:bg-emerald-50/30', 'dark:hover:bg-emerald-950/10'
            ];
            
            if (k === correct) {
                btn.classList.remove(...baseRemove);
                btn.classList.add('border-emerald-400', 'bg-emerald-50/50', 'dark:bg-emerald-950/20', 'dark:border-emerald-500');
                circle.classList.add('bg-emerald-500', 'text-white', 'border-emerald-500');
                circle.classList.remove('bg-white', 'dark:bg-slate-700', 'border-slate-200', 'dark:border-slate-600', 'text-slate-500', 'dark:text-slate-300');
                if (isCorrect) btn.classList.add('pop');
            } else if (k === selected) {
                btn.classList.remove(...baseRemove);
                btn.classList.add('border-rose-400', 'bg-rose-50/50', 'dark:bg-rose-950/20', 'dark:border-rose-500');
                circle.classList.add('bg-rose-500', 'text-white', 'border-rose-500');
                circle.classList.remove('bg-white', 'dark:bg-slate-700', 'border-slate-200', 'dark:border-slate-600', 'text-slate-500', 'dark:text-slate-300');
                btn.classList.add('shake');
            } else {
                btn.classList.add('opacity-40');
            }
        });
    }
    
    // Reveal Feedback & Explanation
    if (testFeedback) {
        testFeedback.innerHTML = isCorrect
            ? '<i class="fas fa-check-circle text-emerald-500 text-lg"></i><span class="text-emerald-600 dark:text-emerald-400 font-extrabold text-sm">Doğru!</span>'
            : `<i class="fas fa-times-circle text-rose-500 text-lg"></i><span class="text-rose-600 dark:text-rose-400 font-extrabold text-sm">Yanlış! Doğru: ${correct}</span>`;
        testFeedback.classList.remove('opacity-0');
        testFeedback.classList.add('opacity-100');
    }
    
    if (explanationText) {
        explanationText.innerHTML = q.explanation.replace(/\n/g, '<br>');
    }
    
    if (solutionBadge) {
        if (q.type === 'turquoise') {
            solutionBadge.textContent = "✨ ALTISI ÇİZİLEN ÇÖZÜM";
            solutionBadge.className = "px-3 py-1 bg-teal-50 dark:bg-teal-950/40 text-teal-600 dark:text-teal-400 text-[10px] font-black rounded uppercase tracking-wider";
        } else {
            solutionBadge.textContent = "🔍 DETAYLI AÇIKLAMA";
            solutionBadge.className = "px-3 py-1 bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-350 text-[10px] font-black rounded uppercase tracking-wider";
        }
    }
    
    if (solutionPanel) {
        solutionPanel.classList.remove('hidden');
        solutionPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    
    if (nextBtn) {
        nextBtn.classList.remove('opacity-0', 'pointer-events-none');
        nextBtn.classList.add('opacity-100');
    }
}

// ── Advance ───────────────────────────────────────────────────────────────
function advance() {
    if (currentIndex >= shuffledQuestions.length - 1) {
        showFinish();
        return;
    }
    currentIndex++;
    
    if (quizContainer) {
        quizContainer.style.opacity = '0';
        quizContainer.style.transform = 'translateY(10px)';
    }
    
    setTimeout(() => {
        loadQuestion();
        if (quizContainer) {
            quizContainer.style.transform = 'translateY(-10px)';
            requestAnimationFrame(() => requestAnimationFrame(() => {
                quizContainer.style.opacity = '1';
                quizContainer.style.transform = 'translateY(0)';
                quizContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }));
        }
    }, 180);
}

// ── Skip ──────────────────────────────────────────────────────────────────
if (skipBtn) {
    skipBtn.addEventListener('click', () => {
        if (answered) return;
        skippedAnswers++;
        advance();
    });
}

if (nextBtn) {
    nextBtn.addEventListener('click', () => {
        if (answered) advance();
    });
}

// ── Keyboard Shortcuts ────────────────────────────────────────────────────
document.addEventListener('keydown', e => {
    // ignore if typing or modal open
    if (document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'TEXTAREA') return;
    
    const key = e.key.toUpperCase();
    if (!answered && ['A', 'B', 'C', 'D', 'E'].includes(key)) {
        if (testOptions) {
            const btn = testOptions.querySelector(`[data-key="${key}"]`);
            if (btn) btn.click();
        }
    } else if (answered && (e.key === 'Enter' || e.key === 'ArrowRight')) {
        advance();
    } else if (!answered && e.key === 'ArrowRight') {
        if (skipBtn) skipBtn.click();
    }
});

// ── Show Finish Screen ─────────────────────────────────────────────────────
function showFinish() {
    if (quizContainer) quizContainer.classList.add('hidden');
    if (finishScreen) {
        finishScreen.classList.remove('hidden');
        finishScreen.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    
    const validTotal = shuffledQuestions.length - skippedAnswers;
    const pct = validTotal > 0 ? Math.round((correctAnswers / validTotal) * 100) : 0;
    
    if (finalScore) {
        finalScore.innerHTML = `Toplam <strong>${shuffledQuestions.length}</strong> sorudan <strong>${correctAnswers}</strong> doğru, <strong>${wrongAnswers}</strong> yanlış ve <strong>${skippedAnswers}</strong> atlama yaptınız.`;
    }
    
    let rating = '';
    let emoji = '🎉';
    if (pct >= 85) {
        rating = `🏆 Kusursuz Başarı! (%${pct})`;
        emoji = '🏆';
    } else if (pct >= 70) {
        rating = `🎯 Harika Performans! (%${pct})`;
        emoji = '🎉';
    } else if (pct >= 50) {
        rating = `📈 Çok İyi, Gelişiyorsun! (%${pct})`;
        emoji = '✨';
    } else {
        rating = `📚 Biraz Daha Tekrar İyi Olur! (%${pct})`;
        emoji = '💪';
    }
    
    if (finalRating) finalRating.textContent = rating;
    if (finishEmoji) finishEmoji.textContent = emoji;
}

// ── Restart Test ──────────────────────────────────────────────────────────
function restartTest() {
    initQuiz();
}

// ── Startup ───────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    initQuiz();
});
