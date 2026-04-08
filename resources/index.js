/* global DATA */
const ICON_PDF = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><text x="12" y="17" text-anchor="middle" font-size="6" fill="currentColor" stroke="none" font-weight="bold">PDF</text></svg>';
const ICON_WORD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><text x="12" y="17" text-anchor="middle" font-size="5" fill="currentColor" stroke="none" font-weight="bold">DOC</text></svg>';
const ICON_HTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><text x="12" y="17" text-anchor="middle" font-size="4.5" fill="currentColor" stroke="none" font-weight="bold">HTML</text></svg>';
const ICON_PRINT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>';
const ICON_VIEW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>';

let currentFolder = "";

const breadcrumbEl = document.getElementById("breadcrumb");
const subfoldersEl = document.getElementById("subfolders");

const indexView = document.getElementById("index-view");
const syllabusView = document.getElementById("syllabus-view");
const syllabusToolbar = document.getElementById("syllabus-toolbar");
const syllabusContent = document.getElementById("syllabus-content");

DATA.forEach(e => {
    const h = e.duration_hours || e.duration_hours_long || 0;
    const hs = e.duration_hours_short || 0;
    e.dh = h;
    e.dh_short = hs;
    e.duration_days = h ? Math.round(h / 8) : 0;
    e.duration_days_short = hs ? Math.round(hs / 8) : 0;
});
const ALL_DURATION_DAYS = [...new Set(DATA.map(e => e.duration_days).filter(d => d > 0))].sort((a, b) => a - b);

const searchEl = document.getElementById("search");
const levelEl = document.getElementById("filter-level");
const categoryEl = document.getElementById("filter-category");
const tagEl = document.getElementById("filter-tag");
const audienceEl = document.getElementById("filter-audience");
const durationEl = document.getElementById("filter-duration");
const sort1El = document.getElementById("sort-primary");
const sort1DirEl = document.getElementById("sort-primary-dir");
const sort2El = document.getElementById("sort-secondary");
const sort2DirEl = document.getElementById("sort-secondary-dir");
const resultsEl = document.getElementById("results");
const totalEl = document.getElementById("total-count");

durationEl.innerHTML = '<option value="">All durations</option>' +
    ALL_DURATION_DAYS.map(d => '<option value="' + d + '">' + d +
    (d === 1 ? " day" : " days") + "</option>").join("");

document.querySelector('label[for="filter-level"]').textContent =
    "Level (" + new Set(DATA.map(e => e.level).filter(Boolean)).size + "):";
document.querySelector('label[for="filter-category"]').textContent =
    "Category (" + new Set(DATA.map(e => e.category).filter(Boolean)).size + "):";
document.querySelector('label[for="filter-tag"]').textContent =
    "Tag (" + new Set(DATA.flatMap(e => e.tags)).size + "):";
document.querySelector('label[for="filter-duration"]').textContent =
    "Duration (" + ALL_DURATION_DAYS.length + "):";
document.querySelector('label[for="filter-audience"]').textContent =
    "Audience (" + new Set(DATA.flatMap(e => e.audience)).size + "):";

function showIndex() {
    syllabusView.style.display = "none";
    indexView.style.display = "";

    window.scrollTo(0, 0);
}

function showSyllabus(path) {
    const base = path.replace(/\.html$/, "");
    indexView.style.display = "none";
    syllabusView.style.display = "";
    syllabusContent.innerHTML = '<p>Loading...</p>';
    syllabusToolbar.innerHTML =
        '<a class="back-btn" href="#" onclick="goBack(); return false;">&larr; Back to index</a>' +
        '<a href="' + base + '.pdf" target="_blank">' + ICON_VIEW + ' View PDF</a>' +
        '<a href="' + base + '.pdf" download>' + ICON_PDF + ' PDF</a>' +
        '<a href="' + base + '.docx" download>' + ICON_WORD + ' Word</a>' +
        '<a href="' + path + '" download>' + ICON_HTML + ' HTML</a>' +
        '<a href="#" onclick="printSyllabus(); return false;">' + ICON_PRINT + ' Print</a>';
    fetch(path)
        .then(function(r) { return r.ok ? r.text() : Promise.reject(r.status); })
        .then(function(html) {
            syllabusContent.innerHTML = html;
            var entry = DATA.find(function(e) { return e.path === path; });

            window.scrollTo(0, 0);
        })
        .catch(function() { syllabusContent.innerHTML = '<p>Failed to load syllabus.</p>'; });
}

function goBack() {
    history.back();
}

function printSyllabus() {
    syllabusToolbar.style.display = "none";
    window.print();
    syllabusToolbar.style.display = "";
}

function printCourse(path) {
    fetch(path)
        .then(function(r) { return r.ok ? r.text() : Promise.reject(r.status); })
        .then(function(html) {
            indexView.style.display = "none";
            syllabusView.style.display = "";
            syllabusToolbar.style.display = "none";
            syllabusContent.innerHTML = html;
            window.print();
            syllabusToolbar.style.display = "";
            syllabusView.style.display = "none";
            indexView.style.display = "";
        });
}

window.addEventListener("popstate", function() {
    var hash = location.hash;
    if (hash && hash.startsWith("#syllabus=")) {
        showSyllabus(decodeURIComponent(hash.substring(10)));
    } else if (hash && hash.startsWith("#folder=")) {
        currentFolder = decodeURIComponent(hash.substring(8));
        indexView.style.display = "";
        syllabusView.style.display = "none";
        render();
    } else {
        currentFolder = "";
        showIndex();
    }
});

function openSyllabus(path) {
    history.pushState(null, "", "#syllabus=" + encodeURIComponent(path));
    showSyllabus(path);
}

function navigateFolder(folder) {
    currentFolder = folder;
    history.pushState(null, "", "#folder=" + encodeURIComponent(folder));
    render();
    window.scrollTo(0, 0);
}

function getSubfolders(folder, entries) {
    const subs = new Map();
    for (const e of entries) {
        if (folder === "") {
            const slash = e.path.indexOf("/");
            if (slash === -1) continue;
            const sub = e.path.substring(0, slash);
            subs.set(sub, (subs.get(sub) || 0) + 1);
        } else {
            const prefix = folder + "/";
            if (!e.path.startsWith(prefix)) continue;
            const rest = e.path.substring(prefix.length);
            const slash = rest.indexOf("/");
            if (slash === -1) continue;
            const sub = rest.substring(0, slash);
            subs.set(sub, (subs.get(sub) || 0) + 1);
        }
    }
    return [...subs.entries()].sort((a, b) => a[0].localeCompare(b[0]));
}

function renderBreadcrumb() {
    if (currentFolder === "") {
        breadcrumbEl.innerHTML = '<span class="breadcrumb-current">home</span>';
        return;
    }
    const parts = currentFolder.split("/");
    let html = '<a href="#" onclick="navigateFolder(\'\'); return false;">home</a>';
    for (let i = 0; i < parts.length; i++) {
        const path = parts.slice(0, i + 1).join("/");
        const label = parts[i].replace(/_/g, " ");
        html += '<span class="breadcrumb-sep">&gt;</span>';
        if (i === parts.length - 1) {
            html += '<span class="breadcrumb-current">' + label + '</span>';
        } else {
            html += '<a href="#" onclick="navigateFolder(\'' + path + '\'); return false;">' + label + '</a>';
        }
    }
    breadcrumbEl.innerHTML = html;
}

function renderSubfolders(filtered) {
    const subs = getSubfolders(currentFolder, filtered);
    if (subs.length === 0) {
        subfoldersEl.innerHTML = "";
        return;
    }
    subfoldersEl.innerHTML = subs.map(function(s) {
        var name = s[0];
        var count = s[1];
        var path = currentFolder ? currentFolder + "/" + name : name;
        var label = name.replace(/_/g, " ");
        return '<a class="subfolder-card" href="#" onclick="navigateFolder(\'' +
            path.replace(/'/g, "\\'") + '\'); return false;">' +
            label + ' <span class="subfolder-count">(' + count + ')</span></a>';
    }).join("");
}

function render() {
    const search = searchEl.value.toLowerCase();
    const level = levelEl.value;
    const category = categoryEl.value;
    const tag = tagEl.value;
    const audience = audienceEl.value;
    const duration = durationEl.value;
    const sort1 = sort1El.value;
    const sort1Dir = sort1DirEl.value === "asc" ? 1 : -1;
    const sort2 = sort2El.value;
    const sort2Dir = sort2DirEl.value === "asc" ? 1 : -1;

    renderBreadcrumb();
    const folderPrefix = currentFolder ? currentFolder + "/" : "";
    const filtered = DATA.filter(e => {
        if (folderPrefix && !e.path.startsWith(folderPrefix)) return false;
        if (search && !e.title.toLowerCase().includes(search)) return false;
        if (level && e.level !== level) return false;
        if (category && e.category.replace(/-/g, " ").toLowerCase() !== category.replace(/-/g, " ").toLowerCase()) return false;
        if (tag && !e.tags.includes(tag)) return false;
        if (audience && !e.audience.some(a => a.replace(/-/g, " ").toLowerCase() === audience.replace(/-/g, " ").toLowerCase())) return false;
        if (duration) {
            const d = parseInt(duration);
            if (e.dh_short) {
                if (d < e.duration_days_short || d > e.duration_days) return false;
            } else if (e.duration_days !== d) return false;
        }
        return true;
    });

    totalEl.textContent = filtered.length + " of " + DATA.length + " syllabi";
    renderSubfolders(filtered);

    const getVal = (e, key) => {
        if (key === "level") return {beginner: 0, intermediate: 1, advanced: 2}[e.level] ?? 3;
        if (key === "duration") return e.dh || 0;
        if (key === "category") return e.folder;
        return e[key];
    };

    const getLabel = (e, key) => {
        if (key === "level") return (e.level || "No Level").charAt(0).toUpperCase() + (e.level || "No Level").slice(1);
        if (key === "duration") return (e.dh ? Math.round(e.dh / 8) + " days" : "No Duration");
        if (key === "category") return e.folder;
        if (key === "title") return "All Syllabi";
        return "";
    };

    filtered.sort((a, b) => {
        const v1a = getVal(a, sort1);
        const v1b = getVal(b, sort1);
        if (v1a !== v1b) {
            const res = (typeof v1a === 'string') ? v1a.localeCompare(v1b) : v1a - v1b;
            return res * sort1Dir;
        }
        const v2a = getVal(a, sort2);
        const v2b = getVal(b, sort2);
        if (v2a !== v2b) {
            const res = (typeof v2a === 'string') ? v2a.localeCompare(v2b) : v2a - v2b;
            return res * sort2Dir;
        }
        return a.title.localeCompare(b.title);
    });

    const groups = [];
    let lastHeader = null;
    for (const item of filtered) {
        const h = getLabel(item, sort1);
        if (h !== lastHeader) {
            groups.push({label: h, items: []});
            lastHeader = h;
        }
        groups[groups.length - 1].items.push(item);
    }

    let html = "";
    if (groups.length === 0) {
        html = '<p class="no-results">No syllabi match the current filters.</p>';
    }
    for (const group of groups) {
        html += "<h2>" + group.label + ' <span class="count">(' + group.items.length + ")</span></h2><ul>";
        for (const item of group.items) {
            const levelClass = item.level ? " level-" + item.level : "";
            const levelBadge = item.level ? '<span class="level' + levelClass + '">' + item.level + "</span>" : "";
            let db = "";
            if (item.dh_short) {
                db = item.duration_days_short + "-" + item.duration_days + "d / " + item.dh_short + "-" + item.dh + "h";
            } else if (item.dh) {
                db = item.duration_days + "d / " + item.dh + "h";
            }
            const durationBadge = db ? '<span class="duration">' + db + "</span>" : "";
            const base = item.path.replace(/\.html$/, "");
            const pdfLink = '<a class="dl-icon" href="' + base + '.pdf" download title="Download PDF">' + ICON_PDF + '</a>';
            const docxLink = '<a class="dl-icon" href="' + base + '.docx" download title="Download Word">' + ICON_WORD + '</a>';
            const htmlLink = '<a class="dl-icon" href="' + item.path + '" download title="Download HTML">' + ICON_HTML + '</a>';
            const printLink = '<a class="dl-icon" href="#" onclick="printCourse(\'' + item.path.replace(/'/g, "\\'") + '\'); return false;" title="Print">' + ICON_PRINT + '</a>';
            html += '<li><a href="#" onclick="openSyllabus(\'' + item.path.replace(/'/g, "\\'") + '\'); return false;">' + item.title + "</a>" + levelBadge + durationBadge + " " + pdfLink + docxLink + htmlLink + printLink + "</li>";
        }
        html += "</ul>";
    }
    resultsEl.innerHTML = html;
}

// Autocomplete
const acList = document.getElementById("autocomplete-list");
let acIndex = -1;

function updateAutocomplete() {
    const query = searchEl.value.toLowerCase();
    acIndex = -1;
    if (query.length < 2) {
        acList.classList.remove("visible");
        return;
    }
    const matches = DATA.filter(e => e.title.toLowerCase().includes(query)).slice(0, 10);
    if (matches.length === 0) {
        acList.classList.remove("visible");
        return;
    }
    acList.innerHTML = matches.map((m, i) =>
        '<div class="autocomplete-item" data-index="' + i + '" data-path="' + m.path + '">' +
        m.title + '<span class="ac-folder">' + m.folder + '</span></div>'
    ).join("");
    acList.classList.add("visible");
}

acList.addEventListener("mousedown", function(ev) {
    var item = ev.target.closest(".autocomplete-item");
    if (item) {
        acList.classList.remove("visible");
        searchEl.value = "";
        openSyllabus(item.dataset.path);
    }
});

searchEl.addEventListener("keydown", function(ev) {
    var items = acList.querySelectorAll(".autocomplete-item");
    if (!acList.classList.contains("visible") || items.length === 0) return;
    if (ev.key === "ArrowDown") {
        ev.preventDefault();
        acIndex = Math.min(acIndex + 1, items.length - 1);
    } else if (ev.key === "ArrowUp") {
        ev.preventDefault();
        acIndex = Math.max(acIndex - 1, 0);
    } else if (ev.key === "Enter" && acIndex >= 0) {
        ev.preventDefault();
        acList.classList.remove("visible");
        searchEl.value = "";
        openSyllabus(items[acIndex].dataset.path);
        return;
    } else if (ev.key === "Escape") {
        acList.classList.remove("visible");
        return;
    } else {
        return;
    }
    items.forEach(function(el, i) {
        el.classList.toggle("active", i === acIndex);
    });
});

searchEl.addEventListener("blur", function() {
    setTimeout(function() { acList.classList.remove("visible"); }, 150);
});

searchEl.addEventListener("input", function() {
    updateAutocomplete();
    render();
});
levelEl.addEventListener("change", render);
categoryEl.addEventListener("change", render);
tagEl.addEventListener("change", render);
audienceEl.addEventListener("change", render);
durationEl.addEventListener("change", render);
sort1El.addEventListener("change", render);
sort1DirEl.addEventListener("change", render);
sort2El.addEventListener("change", render);
sort2DirEl.addEventListener("change", render);

// Handle initial load with hash
if (location.hash && location.hash.startsWith("#syllabus=")) {
    showSyllabus(decodeURIComponent(location.hash.substring(10)));
} else if (location.hash && location.hash.startsWith("#folder=")) {
    currentFolder = decodeURIComponent(location.hash.substring(8));
    render();
} else if (location.hash && location.hash.startsWith("#search=")) {
    searchEl.value = decodeURIComponent(location.hash.substring(8));
    render();
} else {
    render();
}

// Theme switcher
(function() {
    const THEME_KEY = "syllabi-browser-theme";
    const sel = document.getElementById("theme-select");
    const saved = localStorage.getItem(THEME_KEY) || "midnight";

    function applyTheme(name) {
        document.documentElement.setAttribute("data-theme", name);
        sel.value = name;
        localStorage.setItem(THEME_KEY, name);
    }

    sel.addEventListener("change", function() {
        applyTheme(sel.value);
    });

    applyTheme(saved);
})();
