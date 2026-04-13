# Structural Notes for syllabi

## Duration fields

Courses use duration_hours in their `YAML` front-matter. The website derives a virtual
duration_days property (hours / 8) for display and filtering.

Courses that have both a short and long variant use two fields instead:

```yaml
duration_hours_short: 16
duration_hours_long: 40
```

Tag list files exist for all three: duration_hours.txt, duration_hours_short.txt,
duration_hours_long.txt.

## Long/short course variants

Rather than maintaining separate files for short and long versions of a course,
we keep a single file and mark long-only sections or sub-items with `[long]`:

```markdown
## Duration
* Short: 16 hours / 2 days
* Long: 40 hours / 5 days

## Outline
* Python Refresher [long]
    * Data types
    * Control structures
* Core Topic
    * Always covered
    * Deep dive item [long]
```

Topics without a `[long]` tag are included in both versions.

## Deduplication history (2026-03-28)

The following duplicate pairs were resolved:

### Deleted (strictly inferior duplicates)
- languages/`c`/c_programming_old.md — duplicate of c_programming.md
- languages/`java`/java_programming_2.md — duplicate of java_programming.md

### Deleted with unique topics preserved as comments
- operating_systems/`linux`/linux_debugging_old.md — merged unique topics
  (MMU, efence, dmalloc, LD_PRELOAD, etc.) as a comment into linux_debugging.md
- `git`/git_syllabus.md — merged unique topics (packfiles, transfer protocols,
  plumbing vs porcelain, etc.) as a comment into `git`.md

### Renamed for clarity
- machine_learning/machine_learning.md — title changed to
  "Intro to `Machine Learning` with `Python`"
- machine_learning/ml1.md — title changed to
  "`Machine Learning` Theory and Deep Learning"

### Title fix
- databases/`oracle`/oracle_for_administrators.md — title was incorrectly
  "`Oracle` for Developers", fixed to "`Oracle` for Administrators"

### Long/short pairs merged into single files
- languages/`python`/data_analysis_and_scientific_python.md (32h/16h)
- operating_systems/`android`/developing_android_applications_with_java.md (48h/40h)
- operating_systems/`android`/developing_android_applications_with_kotlin.md (48h/40h)
- languages/`python`/practical_machine_learning_using_python.md (40h/16h)
- security/cyber_threats_and_attack_vectors.md (48h/24h)
- security/web_application_hacking.md (40h/16h)
- development_methodologies/development_methodologies.md — same duration (8h),
  unique topics from the short version ("Fail often, fail soon", "Focus",
  "Basic engineering principles") merged into the main outline

## Tracks

Tracks are multi-course learning paths (e.g. bootcamps). They live as YAML files
in `tracks/` and reference courses and chapters from `syllabi/courses/`.

### Track YAML format

```yaml
title: Track Title
tags:
  - infrastructure:aws
  - practices:devops
level: beginner
category: cloud
duration_hours: 400
audience:
  - audiences:developers
description: >
  Multi-line description of the track.
intended_audience:
  - Who this track is for.
prerequisites:
  - What students need before starting.
required_knowledge:
  - Specific courses or skills assumed.
objectives:
  - What students will learn.
exercises:
  - url: https://example.com
    description: External exercise resource
chapters:
  # Include an entire course
  - course: operating_systems/linux/linux_fundamentals
    hours: 40

  # Include specific chapters from a course
  - course: cloud/aws/aws_security
    chapters: [identity-and-access-management-deep-dive, data-protection-and-encryption]
    hours: 16
notes:
  - Optional notes about the track.
```

**Fields:**

| Field | Required | Description |
|---|---|---|
| `title` | yes | Track display name |
| `tags` | yes | Tag list (same format as course frontmatter) |
| `level` | yes | beginner, intermediate, or advanced |
| `category` | yes | Must match a value in `tags/category.txt` |
| `duration_hours` | yes | Total track duration in hours |
| `audience` | yes | Audience tags |
| `description` | yes | Free-text description |
| `intended_audience` | no | Bullet list of who should take this track |
| `prerequisites` | no | Bullet list of prerequisites |
| `required_knowledge` | no | Specific knowledge assumed (distinct from prerequisites) |
| `objectives` | no | Bullet list of learning objectives |
| `exercises` | no | List of `{url, description}` for external resources |
| `chapters` | yes | Ordered list of course references (see below) |
| `notes` | no | Additional notes |

**Chapter references:**

Each entry in `chapters` has:
- `course` (required): path relative to `syllabi/courses/` without `.md` extension
- `hours` (optional): how many hours to allocate for this part
- `chapters` (optional): list of specific chapter IDs to include. If omitted, the entire course outline is included.

Chapter IDs correspond to `<!-- chapter: chapter-id -->` comments in course markdown files.

### Building tracks

`scripts/build_tracks.py` assembles track YAML into complete markdown files.
It runs in batch mode:

```bash
scripts/build_tracks.py source1.yaml target1.md [source2.yaml target2.md ...]
```

The script:
1. Reads the YAML track definition
2. Generates metadata sections (title, description, duration, etc.)
3. For each chapter reference, reads the course markdown and extracts the outline
   (either the full outline or specific chapters by ID)
4. Writes the assembled markdown to the target path

The script is strict — it fails immediately if a referenced course or chapter ID
does not exist.

## Scripts

### scripts/check_md.py

Validates course markdown files. Run in batch mode by rsconstruct.

Checks:
- Exactly one `# Title` heading
- Required sections present: Description, Duration, Intended Audience, Prerequisites, Objectives, Outline, Copyright
- Sections appear in the canonical order defined in `REQUIRED`
- Exactly one `<!-- course: id -->` comment
- Every top-level outline bullet has a `<!-- chapter: id -->` comment before it

### scripts/build_site.py

Generates `docs/index.html` — a single-page application for browsing syllabi.

Workflow:
1. Runs `rsconstruct clean unknown` to remove stale files from `docs/`
2. Scans all `.html` files in `docs/` (produced by pandoc)
3. Reads frontmatter from the corresponding `.md` source for metadata
4. Generates `index.html` from templates in `resources/` with embedded course data

The SPA loads syllabus HTML inline (via fetch) with download links for PDF, Word,
and HTML formats. Pandoc output is never modified.

### scripts/build_tracks.py

Assembles track YAML definitions into complete markdown files. See the Tracks
section above for usage and format details.

## Inconsistent nesting depth
- devops/ mixes loose files (introduction_to_devops.md, architectural_decisions_in_devops.md) with tool sub-folders (`docker`/, `jenkins`/, `terraform`/).
- security/ is flat despite having distinct sub-domains (web security, forensics, exploitation, policy).

## Misplaced files
- architecting/message_queues.md could live under queues/ alongside `Kafka` and `RabbitMQ`.
- big_data/`splunk`/ is more of an observability/monitoring tool and could fit under observability_and_monitoring/.
- operating_systems/`linux`/security/offensive_linux.md is a security topic and could fit under security/.

## Single-file folders
- languages/`opencl`/, languages/`kotlin`/, languages/`r`/, languages/dotnet/, languages/`assembly`/, `unity`/, `wifi`/ each contain only one file.
