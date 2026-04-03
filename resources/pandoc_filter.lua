-- Extract the course path (e.g. "languages/c++") from the input filename.
local function get_course_path()
    local input = PANDOC_STATE.input_files[1] or ""
    local path = input:match("syllabi/courses/(.+)/[^/]+$")
        or input:match("out/generator/(.+)/[^/]+$")
    return path
end

-- Count the directory depth from the input file to the _site root.
local function get_depth()
    local input = PANDOC_STATE.input_files[1] or ""
    local rel = input:match("syllabi/courses/(.+)$")
        or input:match("out/generator/(.+)$")
    if not rel then return 0 end
    local depth = 0
    for _ in rel:gmatch("/") do
        depth = depth + 1
    end
    return depth
end

-- Build the category line: plain text for pdf/docx, linked breadcrumbs for html.
local function build_category_block(course_path)
    local inlines = {pandoc.Strong({pandoc.Str("Category:")}), pandoc.Space()}
    if FORMAT:match("html") then
        local depth = get_depth()
        local prefix = string.rep("../", depth) .. "index.html"
        local segments = {}
        for seg in course_path:gmatch("[^/]+") do
            table.insert(segments, seg)
        end
        for i, seg in ipairs(segments) do
            if i > 1 then
                table.insert(inlines, pandoc.Str(" / "))
            end
            local url = prefix .. "#search=" .. seg
            table.insert(inlines, pandoc.Link({pandoc.Str(seg)}, url))
        end
    else
        table.insert(inlines, pandoc.Str(course_path))
    end
    return pandoc.Para(inlines)
end

-- Set the document title from the first H1 heading if no title is set,
-- remove that H1 to avoid duplication in standalone mode,
-- and insert the course category path.
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
    return doc
end
