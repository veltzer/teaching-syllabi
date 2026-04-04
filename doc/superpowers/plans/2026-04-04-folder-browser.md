# Folder Browser Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an integrated folder browser with breadcrumb navigation and subfolder cards to the index page, allowing users to explore the course hierarchy while keeping all existing filters functional.

**Architecture:** A `currentFolder` state variable tracks the user's position in the folder tree derived from the existing `path` field in DATA entries. The `render()` function is extended to filter by folder prefix, compute subfolders, and render breadcrumbs + subfolder cards above the course list. URL hash `#folder=...` enables deep-linking.

**Tech Stack:** Vanilla JS, CSS — same as existing index page. No new dependencies.

---

### File Structure

- **Modify:** `resources/index.html` — Add breadcrumb and subfolder container divs
- **Modify:** `resources/index.css` — Add styles for breadcrumbs and subfolder cards
- **Modify:** `resources/index.js` — Add folder state, navigation, breadcrumb/subfolder rendering, folder filtering

---

### Task 1: Add HTML containers for breadcrumb and subfolders

**Files:**
- Modify: `resources/index.html:12-14` (after `<div id="index-view">` heading)

- [ ] **Step 1: Add breadcrumb and subfolder divs to index.html**

Insert a breadcrumb bar and a subfolder container between the total-count paragraph and the filters div. Edit `resources/index.html`, replacing:

```html
<p id="total-count">{{TOTAL_COUNT}} courses</p>

<div class="filters">
```

with:

```html
<p id="total-count">{{TOTAL_COUNT}} courses</p>

<div id="breadcrumb"></div>
<div id="subfolders"></div>

<div class="filters">
```

- [ ] **Step 2: Verify build passes**

Run: `rsconstruct build 2>&1 | tail -5`
Expected: Build summary with no errors. The htmlhint and eslint checks must pass.

---

### Task 2: Add CSS styles for breadcrumbs and subfolder cards

**Files:**
- Modify: `resources/index.css` (append at end)

- [ ] **Step 1: Add breadcrumb styles**

Append to `resources/index.css`:

```css
#breadcrumb { margin-bottom: 10px; font-size: 0.95em; }
#breadcrumb a { color: #0366d6; text-decoration: none; }
#breadcrumb a:hover { text-decoration: underline; }
#breadcrumb .breadcrumb-sep { color: #888; margin: 0 6px; }
#breadcrumb .breadcrumb-current { font-weight: bold; color: #333; }
```

- [ ] **Step 2: Add subfolder card styles**

Append to `resources/index.css`:

```css
#subfolders { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; }
#subfolders:empty { margin-bottom: 0; }
.subfolder-card { display: inline-flex; align-items: center; gap: 6px; padding: 8px 14px; background: #f5f5f5; border: 1px solid #ddd; border-radius: 6px; cursor: pointer; font-size: 0.9em; text-decoration: none; color: #333; }
.subfolder-card:hover { background: #e1ecf4; border-color: #0366d6; text-decoration: none; }
.subfolder-card .subfolder-count { color: #888; font-size: 0.85em; }
```

- [ ] **Step 3: Verify build passes**

Run: `rsconstruct build 2>&1 | tail -5`
Expected: Build summary with no errors. Stylelint must pass.

---

### Task 3: Add folder state and navigation functions to JS

**Files:**
- Modify: `resources/index.js:6-7` (after icon constants, before DOM element declarations)

- [ ] **Step 1: Add folder state variable and DOM references**

In `resources/index.js`, after the line:

```js
const ICON_PRINT = '...';
```

and before:

```js
const indexView = document.getElementById("index-view");
```

insert:

```js
let currentFolder = "courses";

const breadcrumbEl = document.getElementById("breadcrumb");
const subfoldersEl = document.getElementById("subfolders");
```

- [ ] **Step 2: Add navigateFolder function**

In `resources/index.js`, after the `openSyllabus` function (after line 116), insert:

```js
function navigateFolder(folder) {
    currentFolder = folder;
    history.pushState(null, "", "#folder=" + encodeURIComponent(folder));
    render();
    window.scrollTo(0, 0);
}
```

- [ ] **Step 3: Add getSubfolders helper function**

In `resources/index.js`, after the `navigateFolder` function, insert:

```js
function getSubfolders(folder, entries) {
    const prefix = folder + "/";
    const subs = new Map();
    for (const e of entries) {
        if (!e.path.startsWith(prefix)) continue;
        const rest = e.path.substring(prefix.length);
        const slash = rest.indexOf("/");
        if (slash === -1) continue;
        const sub = rest.substring(0, slash);
        subs.set(sub, (subs.get(sub) || 0) + 1);
    }
    return [...subs.entries()].sort((a, b) => a[0].localeCompare(b[0]));
}
```

- [ ] **Step 4: Add renderBreadcrumb helper function**

In `resources/index.js`, after the `getSubfolders` function, insert:

```js
function renderBreadcrumb() {
    const parts = currentFolder.split("/");
    let html = "";
    for (let i = 0; i < parts.length; i++) {
        const path = parts.slice(0, i + 1).join("/");
        const label = parts[i].replace(/_/g, " ");
        if (i > 0) html += '<span class="breadcrumb-sep">&gt;</span>';
        if (i === parts.length - 1) {
            html += '<span class="breadcrumb-current">' + label + '</span>';
        } else {
            html += '<a href="#" onclick="navigateFolder(\'' + path + '\'); return false;">' + label + '</a>';
        }
    }
    breadcrumbEl.innerHTML = html;
}
```

- [ ] **Step 5: Add renderSubfolders helper function**

In `resources/index.js`, after the `renderBreadcrumb` function, insert:

```js
function renderSubfolders(filtered) {
    const subs = getSubfolders(currentFolder, filtered);
    if (subs.length === 0) {
        subfoldersEl.innerHTML = "";
        return;
    }
    subfoldersEl.innerHTML = subs.map(function(s) {
        var name = s[0];
        var count = s[1];
        var path = currentFolder + "/" + name;
        var label = name.replace(/_/g, " ");
        return '<a class="subfolder-card" href="#" onclick="navigateFolder(\'' +
            path.replace(/'/g, "\\'") + '\'); return false;">' +
            label + ' <span class="subfolder-count">(' + count + ')</span></a>';
    }).join("");
}
```

- [ ] **Step 6: Verify build passes**

Run: `rsconstruct build 2>&1 | tail -5`
Expected: Build summary with no errors. ESLint must pass (navigateFolder, renderBreadcrumb, renderSubfolders will show as unused warnings until Task 4 wires them in, which is acceptable since the eslint rule is "warn" not "error").

---

### Task 4: Integrate folder filtering into render() and URL handling

**Files:**
- Modify: `resources/index.js` — modify `render()`, `popstate` handler, and initial load block

- [ ] **Step 1: Add folder filtering to render()**

In `resources/index.js`, in the `render()` function, find the line:

```js
    const filtered = DATA.filter(e => {
```

Replace it with:

```js
    renderBreadcrumb();
    const folderPrefix = currentFolder + "/";
    const filtered = DATA.filter(e => {
        if (!e.path.startsWith(folderPrefix)) return false;
```

- [ ] **Step 2: Add renderSubfolders call in render()**

In the `render()` function, find the line:

```js
    totalEl.textContent = filtered.length + " of " + DATA.length + " courses";
```

Insert after it:

```js
    renderSubfolders(filtered);
```

- [ ] **Step 3: Update popstate handler for folder hash**

In `resources/index.js`, replace the popstate handler:

```js
window.addEventListener("popstate", function() {
    var hash = location.hash;
    if (hash && hash.startsWith("#syllabus=")) {
        showSyllabus(decodeURIComponent(hash.substring(10)));
    } else {
        showIndex();
    }
});
```

with:

```js
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
        currentFolder = "courses";
        showIndex();
    }
});
```

- [ ] **Step 4: Update initial load block for folder hash**

In `resources/index.js`, replace the initial load block:

```js
// Handle initial load with hash
if (location.hash && location.hash.startsWith("#syllabus=")) {
    showSyllabus(decodeURIComponent(location.hash.substring(10)));
} else if (location.hash && location.hash.startsWith("#search=")) {
    searchEl.value = decodeURIComponent(location.hash.substring(8));
    render();
} else {
    render();
}
```

with:

```js
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
```

- [ ] **Step 5: Verify build passes**

Run: `rsconstruct build 2>&1 | tail -5`
Expected: Build summary with no errors. All linters pass.

- [ ] **Step 6: Verify in browser**

Open `_site/index.html` in a browser. Verify:
1. Breadcrumb shows "courses" at the top
2. Subfolder cards appear (ai, architecting, big_data, etc.) with course counts
3. Clicking a subfolder card navigates into it (breadcrumb updates, subfolders update, course list filters)
4. Clicking a breadcrumb segment navigates back up
5. All existing filters still work within the selected folder
6. Browser back/forward buttons work
7. Deep-linking with `#folder=courses/languages/c++` works
