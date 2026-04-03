-- Set the document title from the first H1 heading if no title is set,
-- and remove that H1 to avoid duplication in standalone mode.
function Pandoc(doc)
    if doc.meta.title then
        return nil
    end
    for i, block in ipairs(doc.blocks) do
        if block.t == "Header" and block.level == 1 then
            doc.meta.title = block.content
            table.remove(doc.blocks, i)
            return doc
        end
    end
end
