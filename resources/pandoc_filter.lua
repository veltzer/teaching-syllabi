-- Extract the course path (e.g. "languages/c++") from the input filename.
local function get_course_path()
    local input = PANDOC_STATE.input_files[1] or ""
    local path = input:match("syllabi/courses/(.+)/[^/]+$")
        or input:match("out/generator/(.+)/[^/]+$")
    return path
end

-- Set the document title from the first H1 heading if no title is set,
-- remove that H1 to avoid duplication in standalone mode,
-- and insert the course path as a subtitle.
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
        local path_block = pandoc.Para({
            pandoc.Emph({pandoc.Str(course_path)})
        })
        table.insert(doc.blocks, 1, path_block)
    end
    return doc
end
