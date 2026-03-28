# Structural Notes for syllabi

## Duration fields

Courses use `duration_hours` in their YAML front-matter. The website derives a virtual
`duration_days` property (hours / 8) for display and filtering.

Courses that have both a short and long variant use two fields instead:

```yaml
duration_hours_short: 16
duration_hours_long: 40
```

Tag list files exist for all three: `duration_hours.txt`, `duration_hours_short.txt`,
`duration_hours_long.txt`.

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
- `languages/c/c_programming_old.md` — duplicate of `c_programming.md`
- `languages/java/java_programming_2.md` — duplicate of `java_programming.md`

### Deleted with unique topics preserved as comments
- `operating_systems/linux/linux_debugging_old.md` — merged unique topics
  (`MMU`, `efence`, `dmalloc`, `LD_PRELOAD`, etc.) as a comment into `linux_debugging.md`
- `git/git_syllabus.md` — merged unique topics (`packfiles`, transfer protocols,
  plumbing vs porcelain, etc.) as a comment into `git.md`

### Renamed for clarity
- `machine_learning/machine_learning.md` — title changed to
  "Intro to Machine Learning with Python"
- `machine_learning/ml1.md` — title changed to
  "Machine Learning Theory and Deep Learning"

### Title fix
- `databases/oracle/oracle_for_administrators.md` — title was incorrectly
  "Oracle for Developers", fixed to "Oracle for Administrators"

### Long/short pairs merged into single files
- `languages/python/data_analysis_and_scientific_python.md` (32h/16h)
- `operating_systems/android/developing_android_applications_with_java.md` (48h/40h)
- `operating_systems/android/developing_android_applications_with_kotlin.md` (48h/40h)
- `languages/python/practical_machine_learning_using_python.md` (40h/16h)
- `security/cyber_threats_and_attack_vectors.md` (48h/24h)
- `security/web_application_hacking.md` (40h/16h)
- `development_methodologies/development_methodologies.md` — same duration (8h),
  unique topics from the short version ("Fail often, fail soon", "Focus",
  "Basic engineering principles") merged into the main outline

## Deferred

- `tracks/` directory: tracks are meant to be collections of concatenated courses.
  `tracks/aws_for_experienced_developers.md` currently duplicates course content
  instead of referencing courses. To be redesigned later.

## Inconsistent nesting depth
- `devops/` mixes loose files (`introduction_to_devops.md`, `architectural_decisions_in_devops.md`) with tool sub-folders (`docker/`, `jenkins/`, `terraform/`).
- `security/` is flat despite having distinct sub-domains (web security, forensics, exploitation, policy).

## Misplaced files
- `architecting/message_queues.md` could live under `queues/` alongside Kafka and RabbitMQ.
- `big_data/splunk/` is more of an observability/monitoring tool and could fit under `observability_and_monitoring/`.
- `operating_systems/linux/security/offensive_linux.md` is a security topic and could fit under `security/`.

## Single-file folders
- `languages/opencl/`, `languages/kotlin/`, `languages/r/`, `languages/dotnet/`, `languages/assembly/`, `unity/`, `wifi/` each contain only one file.
