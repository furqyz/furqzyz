// ─── SIDEBAR AÇ/KAPAT ─────────────────────────────────────────────────────────
function toggleSidebarSection(id, btn) {
    const el = document.getElementById(id);
    const chevron = document.getElementById(id + '-chevron');
    if (!el) return;
    const isHidden = el.classList.contains('hidden');
    el.classList.toggle('hidden', !isHidden);
    if (chevron) chevron.style.transform = isHidden ? 'rotate(180deg)' : 'rotate(0deg)';
}

document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('dark-mode-toggle');

    if (toggleBtn) {
        const applyTheme = (isDark) => {
            if (isDark) {
                document.documentElement.classList.add('dark');
                document.body.classList.add('dark');
                localStorage.setItem('dark-mode', 'true');
            } else {
                document.documentElement.classList.remove('dark');
                document.body.classList.remove('dark');
                localStorage.setItem('dark-mode', 'false');
            }
        };

        // Let HTML inline script set the initial state, then we sync here if needed
        const isCurrentlyDark = document.documentElement.classList.contains('dark');
        
        // Remove cloned button logic as we don't have inline event listener conflicts anymore
        toggleBtn.addEventListener('click', () => {
            const currentDark = document.documentElement.classList.contains('dark');
            applyTheme(!currentDark);
        });
    }

    // Arama vurgulama (Highlight) mantığı
    const urlParams = new URLSearchParams(window.location.search);
    const searchQuery = urlParams.get('search');

    if (searchQuery) {
        const query = searchQuery.toLowerCase();
        let firstMatch = null;

        const walkDOM = (node) => {
            if (node.nodeType === 3) { // Text node
                const text = node.nodeValue;
                const lowerText = text.toLowerCase();
                const index = lowerText.indexOf(query);
                
                if (index !== -1 && node.parentNode.nodeName !== 'SCRIPT' && node.parentNode.nodeName !== 'STYLE') {
                    const originalText = text.substring(index, index + query.length);
                    const beforeText = text.substring(0, index);
                    const afterText = text.substring(index + query.length);
                    
                    const span = document.createElement('span');
                    span.className = 'search-highlight bg-yellow-300 dark:bg-yellow-700 text-slate-900 dark:text-white font-bold rounded px-1 transition-all duration-300 shadow-sm shadow-yellow-500/50 outline outline-2 outline-yellow-400';
                    span.textContent = originalText;
                    
                    const parent = node.parentNode;
                    if (beforeText) parent.insertBefore(document.createTextNode(beforeText), node);
                    parent.insertBefore(span, node);
                    
                    const afterNode = document.createTextNode(afterText);
                    parent.insertBefore(afterNode, node);
                    
                    parent.removeChild(node);
                    
                    if (!firstMatch) firstMatch = span;
                    walkDOM(afterNode);
                }
            } else if (node.nodeType === 1 && !/(script|style|textarea)/i.test(node.tagName)) {
                Array.from(node.childNodes).forEach(walkDOM);
            }
        };

        const mainContent = document.querySelector('main');
        if (mainContent) {
            walkDOM(mainContent);
        }

        if (firstMatch) {
            setTimeout(() => {
                firstMatch.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }, 300);
        }

        const removeHighlights = () => {
            document.querySelectorAll('.search-highlight').forEach(span => {
                const parent = span.parentNode;
                parent.replaceChild(document.createTextNode(span.textContent), span);
                parent.normalize();
            });
            const url = new URL(window.location);
            url.searchParams.delete('search');
            window.history.replaceState({}, '', url);
        };

        setTimeout(() => {
            document.addEventListener('click', removeHighlights, { once: true });
        }, 100);
    }

    // Arama Mantığı
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');

    if (searchInput && searchResults) {
        // Find depth of current page relative to root
        const isSubDir = window.location.pathname.includes('/unitler/') || 
                         window.location.pathname.includes('/turkce/') || 
                         window.location.pathname.includes('/cografya/') ||
                         window.location.pathname.includes('\\cografya\\') ||
                         window.location.pathname.includes('\\unitler\\') ||
                         window.location.pathname.includes('\\turkce\\');
        const prefix = isSubDir ? '../' : '';
        
        const path = window.location.pathname.toLowerCase();
        let indexName = 'searchIndex.js';
        
        if (path.includes('cografya') || path.includes('/cografya/') || path.includes('\\cografya\\')) {
            indexName = 'searchIndex_cografya.js';
        } else if (path.includes('turkce') || path.includes('/turkce/') || path.includes('\\turkce\\')) {
            indexName = 'searchIndex_turkce.js';
        }
        
        const scriptPath = prefix + 'assets/js/' + indexName;
        
        const script = document.createElement('script');
        script.src = scriptPath;
        script.onerror = () => {
            // searchIndex yüklenemedi, arama kutusu gizleniyor
            const searchBox = searchInput.closest('div');
            if (searchBox) searchBox.style.display = 'none';
        };
        document.body.appendChild(script);

        script.onload = () => {
            if (typeof searchIndex === 'undefined') return;
            
            searchInput.addEventListener('input', (e) => {
                const query = e.target.value.toLowerCase().trim();
                
                if (query.length < 2) {
                    searchResults.classList.add('hidden');
                    searchResults.classList.remove('flex');
                    return;
                }

                // Arama filtresi
                const results = searchIndex.filter(item => 
                    item.title.toLowerCase().includes(query) || 
                    item.content.toLowerCase().includes(query) ||
                    item.unit.toLowerCase().includes(query)
                ).slice(0, 8); // En fazla 8 sonuç göster

                if (results.length === 0) {
                    searchResults.innerHTML = '<div class="p-4 text-center text-sm text-slate-500 font-medium">Sonuç bulunamadı.</div>';
                } else {
                    searchResults.innerHTML = results.map(item => {
                        let targetUrl = isSubDir ? `../${item.url}` : item.url;
                        targetUrl += `?search=${encodeURIComponent(query)}`;

                        let displayContent = item.content;
                        if (displayContent.startsWith(item.title)) {
                            displayContent = displayContent.substring(item.title.length).trim();
                        }

                        return `
                            <a href="${targetUrl}" class="p-3 hover:bg-slate-50 dark:hover:bg-slate-700/50 transition-colors cursor-pointer group flex flex-col">
                                <span class="text-[10px] font-black text-indigo-500 dark:text-indigo-400 mb-1 uppercase tracking-widest">${item.unit}</span>
                                <span class="hidden">${item.title}</span>
                                <span class="text-sm font-medium text-slate-800 dark:text-slate-200 group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors line-clamp-2">${displayContent}</span>
                            </a>
                        `;
                    }).join('');
                }
                
                searchResults.classList.remove('hidden');
                searchResults.classList.add('flex');
            });

            // Dışarı tıklanınca sonuç kutusunu gizle
            document.addEventListener('click', (e) => {
                if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
                    searchResults.classList.add('hidden');
                    searchResults.classList.remove('flex');
                }
            });
            
            // Inputa tekrar tıklanınca daha önce sonuç varsa göster
            searchInput.addEventListener('click', () => {
                if (searchInput.value.length >= 2) {
                    searchResults.classList.remove('hidden');
                    searchResults.classList.add('flex');
                }
            });
        };
    }

    // Dynamic Back to Top Button
    const backToTopBtn = document.createElement('button');
    backToTopBtn.className = 'back-to-top-btn';
    backToTopBtn.innerHTML = '<i class="fas fa-arrow-up text-lg"></i>';
    backToTopBtn.setAttribute('title', 'Yukarı Git');
    document.body.appendChild(backToTopBtn);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopBtn.classList.add('show');
        } else {
            backToTopBtn.classList.remove('show');
        }
    });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Dynamic Focus Mode Button (for pages missing it, like TÜİK pages)
    let focusBtn = document.getElementById('focus-mode-btn');
    if (!focusBtn) {
        let focusControls = document.querySelector('.focus-controls');
        if (!focusControls) {
            focusControls = document.createElement('div');
            focusControls.className = 'focus-controls';
            document.body.appendChild(focusControls);
        }
        
        focusBtn = document.createElement('button');
        focusBtn.id = 'focus-mode-btn';
        focusBtn.className = 'focus-btn';
        focusBtn.setAttribute('title', 'Odaklanma Modu (Sadece Notlar)');
        focusBtn.innerHTML = '<i class="fas fa-expand"></i>';
        focusControls.appendChild(focusBtn);
        
        // Dynamically toggle focus mode
        focusBtn.addEventListener('click', () => {
            const body = document.body;
            body.classList.toggle('focus-mode');
            focusBtn.classList.toggle('active');
            const icon = focusBtn.querySelector('i');
            if (body.classList.contains('focus-mode')) {
                icon.className = 'fas fa-compress';
            } else {
                icon.className = 'fas fa-expand';
            }
        });
    }

    // Dynamic Test Çöz Button in the Sidebar Navigation (injects at the top of the menu)
    const cografyaNav = document.getElementById('cografyaNav');
    if (cografyaNav) {
        let testCozBtn = document.getElementById('sidebar-test-coz-btn');
        if (!testCozBtn) {
            const isSubDir = window.location.pathname.includes('/unitler/') || 
                             window.location.pathname.includes('/turkce/') || 
                             window.location.pathname.includes('/cografya/') ||
                             window.location.pathname.includes('\\cografya\\') ||
                             window.location.pathname.includes('\\unitler\\') ||
                             window.location.pathname.includes('\\turkce\\');
            const href = isSubDir ? 'test-coz.html' : 'cografya/test-coz.html';
            
            const btnWrapper = document.createElement('div');
            btnWrapper.id = 'sidebar-test-coz-btn';
            btnWrapper.className = 'mb-4 px-1';
            btnWrapper.innerHTML = `
                <a href="${href}" class="w-full flex items-center justify-center gap-2 bg-gradient-to-r from-teal-500 to-emerald-600 hover:from-teal-600 hover:to-emerald-700 text-white py-3 px-4 rounded-xl font-extrabold text-sm transition-transform hover:scale-[1.03] shadow-md shadow-emerald-200/50 dark:shadow-emerald-900/30">
                    <i class="fas fa-play-circle text-base"></i>
                    <span>TEST ÇÖZ (Çıkmış Sorular)</span>
                </a>
            `;
            cografyaNav.insertBefore(btnWrapper, cografyaNav.firstChild);
        }
    }
});
