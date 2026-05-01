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
    const body = document.body;

    // Sistem tercihini veya kaydedilmiş tercihi kontrol et
    if (localStorage.getItem('dark-mode') === 'true') {
        body.classList.add('dark');
    } else if (localStorage.getItem('dark-mode') === null && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        body.classList.add('dark');
    }

    toggleBtn.addEventListener('click', () => {
        body.classList.toggle('dark');
        localStorage.setItem('dark-mode', body.classList.contains('dark'));
    });

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
        const pathSegments = window.location.pathname.split('/').filter(p => p);
        const isSubDir = window.location.pathname.includes('/unitler/') || window.location.pathname.includes('/turkce/');
        const prefix = isSubDir ? '../' : '';
        
        const isTurkce = window.location.pathname.includes('turkce');
        // If we're in turkce, maybe load searchIndex_turkce.js (if it exists) later.
        // For now, let's keep loading the main searchIndex.js but fix the path
        const scriptPath = prefix + 'assets/js/searchIndex.js';
        
        const script = document.createElement('script');
        script.src = scriptPath;
        document.body.appendChild(script);

        script.onload = () => {
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
                        // For history items
                        let targetUrl = isSubDir ? 
                            (item.unit_id === 1 ? '../index.html' : `../unitler/unite${item.unit_id}.html`) : 
                            (item.unit_id === 1 ? 'index.html' : `unitler/unite${item.unit_id}.html`);
                            
                        // If current page is in unitler, targetUrl to another unit is just `uniteX.html`
                        if (window.location.pathname.includes('/unitler/')) {
                            targetUrl = item.unit_id === 1 ? '../index.html' : `unite${item.unit_id}.html`;
                        }
                            
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
});
