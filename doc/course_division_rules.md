# Rules for Division of Material Across Courses

## Rule 1: Never Have Two Courses at the Same Level for the Same Subject
- This is the most fundamental rule. There must never be two courses covering the same subject at the same level.
- If two such courses exist, they must be merged into one or clearly differentiated (e.g., one becomes beginner, the other advanced).
- Every topic must have exactly one course that "owns" it at each level.

## Rule 2: Introduction Courses Must Be Beginner Level
- Every course named introduction_to_* must have `level: beginner` in its frontmatter.
- If an introduction course requires significant prior knowledge, reconsider the name — it may be better named as a regular or intermediate course.

## Rule 4: Advanced Courses Must Be Advanced Level
- Every course named advanced_* must have `level: advanced` in its frontmatter.
- If a course named "advanced" is actually intermediate, either rename it or change the level.

## Rule 3: A Course Should Not Teach a Topic Covered by Another Course
- If a topic has its own dedicated course, other courses must not teach that topic — they may reference or mention it, but not include it in their outline.
- If a customer needs both topics together, define a track that combines the individual courses.
- Example: a `Kubernetes` course should not include a `Docker` section if a dedicated `Docker` course exists. Instead, create a track that sequences `Docker` followed by `Kubernetes`.

## Rule 5: Prerequisites vs Required Knowledge
- `## Prerequisites` lists **general skills and experience** that are not tied to a specific course in our catalog. Examples: "tech savvy", "programming experience in at least one language", "familiarity with `Linux` command line", "basic networking knowledge", "understanding of web applications".
- `## Required Knowledge` lists **specific topics that have their own course** in our catalog. Examples: "`Docker` Fundamentals", "Introduction to `Git`", "`Bash` Scripting". The customer either takes that course first or confirms equivalent knowledge.
- A prerequisite should never name a specific technology that we have a course for — that belongs in Required Knowledge.
- This distinction helps sales: if a customer picks a course and lacks the Required Knowledge, we can offer to bundle the prerequisite course(s) as a track.
- This replaces embedding another course's material — instead of teaching `Docker` inside a `Kubernetes` course, list `Docker` as required knowledge.

## No Duplicate Courses
- Beginner/Advanced pairs for the same topic are fine (e.g., `sql`.md + advanced_sql.md), but their content must not overlap.

## Beginner/Advanced Progression
- A beginner course must not assume knowledge of the topic itself.
- An advanced course must explicitly list the beginner course (or equivalent experience) as a prerequisite.
- The advanced course must not repeat material from the beginner course.

## Technology Mentions vs. Dedicated Coverage
- A course may mention a related technology in passing (e.g., a `Docker` course mentioning `Kubernetes`) without needing to own that topic.
- If a topic gets more than one outline bullet in a course that doesn't own it, consider whether a dedicated course is needed.
- Track gap comments (`<!-- Track gap: ... -->`) may be used to note subtopics that a course should consider adding.

## Courses in Different Directories
- The same technology should not have standalone courses in multiple directories (e.g., containers/`kubernetes`.md and devops/`kubernetes`/introduction_to_kubernetes.md should be consolidated or clearly differentiated in scope).
- The directory path should reflect the primary audience/context, not create ambiguity.

## Tracks vs. Individual Courses
- Tracks are multi-course bundles (bootcamps). They reference individual courses, not duplicate their content.
- Every topic section in a track must be covered by at least one individual course.
- Tracks may specify different hour allocations than the individual course — the track hours reflect how much of that course is used in the bootcamp context.

## Required Frontmatter
- Every syllabus (course or track) must have: tags, level, category, duration_hours (or duration_hours_short/duration_hours_long), and audience.
- audience entries must only use audiences: prefix tags.
- Tags must exist in the corresponding tag_lists/*.txt file.

## Duration Guidelines
- Standard course durations: 8, 16, 24, 32, 40 hours.
- Longer durations (56, 64, 80, 96) are for deep-dive or comprehensive courses.
- Bootcamp/track durations can be any value.
- The duration_hours in frontmatter must match the duration stated in the `## Duration` section of the body.

## When to Split vs. Merge
- Split a course if it covers two largely independent technologies (e.g., "`Jenkins` and `Gradle`" is fine as a track but each should also exist as an individual course).
- Merge courses if they cover the same technology at the same level and cannot be clearly differentiated by audience or depth.
- A single course should not exceed 40 hours unless it is a deep-dive or comprehensive course with a clear justification.
