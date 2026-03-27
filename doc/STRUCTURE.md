# Structural Notes for syllabi/atoms

These are structural observations that were raised and reviewed. All were considered and rejected by the project owner.

## Inconsistent nesting depth
- `devops/` mixes loose files (`introduction_to_devops.md`, `architectural_decisions_in_devops.md`) with tool sub-folders (`docker/`, `jenkins/`, `terraform/`).
- `security/` is flat despite having distinct sub-domains (web security, forensics, exploitation, policy).

## Misplaced files
- `architecting/message_queues.md` could live under `queues/` alongside Kafka and RabbitMQ.
- `big_data/splunk/` is more of an observability/monitoring tool and could fit under `observability_and_monitoring/`.
- `operating_systems/linux/security/offensive_linux.md` is a security topic and could fit under `security/`.

## Potential merges/deduplication
- `git/git.md` and `git/git_syllabus.md` may overlap significantly.
- `operating_systems/linux/linux_debugging.md` vs `linux_debugging_old.md` — if the old version is superseded, it could be removed.
- `languages/c/c_programming.md` vs `c_programming_old.md` — same situation.

## Single-file folders
- `languages/opencl/`, `languages/kotlin/`, `languages/r/`, `languages/dotnet/`, `languages/assembly/`, `unity/`, `wifi/` each contain only one file.
