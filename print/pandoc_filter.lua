-- Pandoc Lua filter. pandoc injects the `pandoc` module, PANDOC_STATE and
-- FORMAT as globals and picks up the filter by the RawBlock/RawInline/Pandoc
-- globals it defines, so those are declared here rather than in the shared
-- fleet-wide .luacheckrc.
-- luacheck: read globals pandoc PANDOC_STATE FORMAT
-- luacheck: globals RawBlock RawInline Pandoc

-- Extract the course path (e.g. "languages/c++") from the input filename.
local function get_course_path()
    local input = PANDOC_STATE.input_files[1] or ""
    local path = input:match("syllabi/courses/(.+)/[^/]+$")
        or input:match("out/processor%.generator%.generic/(.+)/[^/]+$")
    return path
end

-- Build the category line: plain text for pdf/docx, linked breadcrumbs for html.
local function build_category_block(course_path)
    local inlines = {pandoc.Strong({pandoc.Str("Category:")}), pandoc.Space()}
    if FORMAT:match("html") then
        local segments = {}
        for seg in course_path:gmatch("[^/]+") do
            table.insert(segments, seg)
        end
        for i, seg in ipairs(segments) do
            if i > 1 then
                table.insert(inlines, pandoc.Str(" / "))
            end
            -- Build the full folder path: courses/seg1/seg2/...
            local folder_parts = {"courses"}
            for j = 1, i do
                table.insert(folder_parts, segments[j])
            end
            local folder = table.concat(folder_parts, "/")
            -- Use fragment-only URL since the syllabus is viewed inline
            -- within the index page via fetch + innerHTML.
            local url = "#folder=" .. folder
            table.insert(inlines, pandoc.Link({pandoc.Str(seg)}, url))
        end
    else
        table.insert(inlines, pandoc.Str(course_path))
    end
    return pandoc.Para(inlines)
end

-- Strip <!-- chapter: ..., duration: ... --> comments from output.
function RawBlock(el)
    if el.format == "html" and el.text:match("^%s*<!%-%-.*chapter:.*%-%->%s*$") then
        return {}
    end
end

function RawInline(el)
    if el.format == "html" and el.text:match("<!%-%-.*chapter:.*%-%->") then
        return {}
    end
end

-- Set the document title from the first H1 heading if no title is set,
-- remove that H1 to avoid duplication in standalone mode,
-- and insert the course category path.
-- shared-themes' theme-onload.js, inlined at the start of the body of every
-- HTML syllabus so the theme a reader chose on the sites follows them here.
-- A raw block at the body start rather than header-includes: it works in
-- pandoc and rspandoc alike, and runs before any content is painted.
local function theme_onload_block()
    local f = io.open("shared/shared-themes/theme-onload.js", "r")
    if not f then
        error("shared/shared-themes/theme-onload.js not found; run: git submodule update --init")
    end
    local js = f:read("a")
    f:close()
    return pandoc.RawBlock("html", "<script>\n" .. js .. "</script>")
end

-- shared-themes' LaTeX theme, added to the preamble of every PDF syllabus:
-- the palette's colors and fonts, as themes.css gives the HTML. A raw latex
-- block in header-includes rather than --include-in-header, because the
-- same pandoc arguments render the html and docx too, and those writers
-- drop a raw latex block where they would paste an included file verbatim.
-- Print has no switcher, so it is the fleet's default palette, azure; the
-- docx gets the same through --reference-doc in rsconstruct.toml.
local function latex_theme_block()
    local path = "shared/shared-themes/latex/azure.tex"
    local f = io.open(path, "r")
    if not f then
        error(path .. " not found; run: git submodule update --init")
    end
    local tex = f:read("a")
    f:close()
    return pandoc.RawBlock("latex", tex)
end

function Pandoc(doc)
    if not doc.meta.title then
        for i, block in ipairs(doc.blocks) do
            if block.t == "Header" and block.level == 1 then
                doc.meta.title = block.content
                table.remove(doc.blocks, i)
                break
            end
        end
    end
    local course_path = get_course_path()
    if course_path then
        table.insert(doc.blocks, 1, build_category_block(course_path))
    end
    if FORMAT:match("html") then
        table.insert(doc.blocks, 1, theme_onload_block())
    end
    if FORMAT == "latex" then
        local includes = doc.meta["header-includes"]
        if includes == nil then
            includes = pandoc.MetaList({})
        elseif pandoc.utils.type(includes) ~= "List" then
            includes = pandoc.MetaList({includes})
        end
        includes:insert(pandoc.MetaBlocks({latex_theme_block()}))
        doc.meta["header-includes"] = includes
    end
    return doc
end
