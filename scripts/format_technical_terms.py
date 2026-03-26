#!/usr/bin/env python
"""
Script to add backticks around technical terms in markdown files.
"""
import os
import re
import glob
from typing import List, Tuple

# Define common technical terms that need backticks
TECHNICAL_TERMS = [
    # Programming languages
    'Python', 'Java', 'JavaScript', 'C', 'C++', 'Rust', 'Go', 'Kotlin', 'R', 'SQL', 'HTML', 'CSS',

    # Technologies and frameworks
    'Docker', 'Kubernetes', 'k8s', 'Spring', 'Spring Boot', 'React', 'Angular', 'Vue', 'Django', 'Flask',
    'Kafka', 'RabbitMQ', 'Redis', 'MongoDB', 'PostgreSQL', 'MySQL', 'Oracle', 'ElasticSearch', 'Splunk',
    'Hadoop', 'Spark', 'Hive', 'HDFS',

    # DevOps tools
    'Jenkins', 'Ansible', 'Terraform', 'Puppet', 'Maven', 'Gradle', 'Git', 'GitHub', 'GitLab',
    'Docker Compose', 'Helm', 'Minikube', 'ArgoCD',

    # Cloud platforms
    'AWS', 'Azure', 'GCP', 'Google Cloud',

    # Operating systems
    'Linux', 'Ubuntu', 'Windows', 'macOS', 'CentOS', 'RHEL', 'FreeRTOS',

    # Protocols and formats
    'HTTP', 'HTTPS', 'TCP', 'UDP', 'REST', 'GraphQL', 'JSON', 'XML', 'YAML', 'CSV',

    # Build systems and tools
    'Make', 'GNU Make', 'CMake', 'Makefile', 'Makefiles', 'npm', 'pip', 'yarn',

    # Libraries and packages
    'NumPy', 'Pandas', 'Matplotlib', 'scikit-learn', 'TensorFlow', 'PyTorch', 'jQuery', 'Bootstrap',
    'JUnit', 'Mockito', 'Selenium', 'pytest', 'unittest',

    # File types and extensions
    'Dockerfile', 'package.json', 'requirements.txt', 'pom.xml', 'build.gradle',

    # Command line tools
    'sudo', 'ssh', 'curl', 'wget', 'grep', 'awk', 'sed', 'find', 'ps', 'top', 'htop',
    'docker', 'kubectl', 'helm', 'terraform', 'ansible-playbook',

    # Function/method names (common ones)
    'malloc', 'printf', 'scanf', 'main', 'def', 'class', 'import', 'from', 'return',
    'pthread_create', 'pthread_join', 'fork', 'exec',

    # JVM related
    'JVM', 'JIT', 'GC', 'JDK', 'JRE', 'JNI',

    # IDEs and editors
    'PyCharm', 'IntelliJ', 'VSCode', 'vim', 'emacs', 'Eclipse',

    # Virtualization
    'VirtualBox', 'VMware', 'Hyper-V', 'QEMU',

    # Networking
    'nginx', 'Apache', 'Tomcat', 'IIS',

    # Security
    'SSL', 'TLS', 'HTTPS', 'OAuth', 'JWT', 'LDAP',

    # Monitoring
    'Grafana', 'Prometheus', 'Nagios', 'Zabbix', 'ELK',

    # Package managers
    'apt', 'yum', 'dnf', 'brew', 'chocolatey'
]


def should_add_backticks(text: str, start: int, end: int) -> bool:
    """Check if we should add backticks around this term occurrence."""
    # Don't add if already has backticks
    if start > 0 and text[start-1] == '`':
        return False
    if end < len(text) and text[end] == '`':
        return False

    # Don't add if it's part of a URL
    if 'http' in text[max(0, start-10):start]:
        return False

    # Don't add if it's in a code block (between triple backticks)
    before_text = text[:start]
    code_blocks = before_text.count('```')
    if code_blocks % 2 == 1:  # Odd number means we're inside a code block
        return False

    # Don't add if it's part of a larger word (check word boundaries)
    if start > 0 and text[start-1].isalnum():
        return False
    if end < len(text) and text[end].isalnum():
        return False

    return True

def format_technical_terms(content: str) -> Tuple[str, List[str]]:
    """Add backticks around technical terms."""
    changes = []

    # Sort terms by length (longest first) to avoid partial matches
    sorted_terms = sorted(TECHNICAL_TERMS, key=len, reverse=True)

    for term in sorted_terms:
        # Create regex pattern for word boundaries
        pattern = r'\b' + re.escape(term) + r'\b'

        def replace_match(match):
            start = match.start()
            end = match.end()

            if should_add_backticks(content, start, end):
                changes.append("Added backticks")
                return f'`{match.group()}`'
            return match.group()

        content = re.sub(pattern, replace_match, content, flags=re.IGNORECASE)

    return content, changes

def process_file(file_path: str) -> Tuple[bool, List[str]]:
    """Process a single markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()

    formatted_content, changes = format_technical_terms(original_content)

    if formatted_content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
        return True, changes

    return False, []

def main():
    """Main function to process all markdown files."""
    syllabi_dir = '/home/mark/git/veltzer/teaching-syllabi/syllabi'

    # Find all markdown files
    md_files = glob.glob(os.path.join(syllabi_dir, '**/*.md'), recursive=True)

    print(f"Found {len(md_files)} markdown files to process...")

    total_changed = 0
    all_changes = {}

    for file_path in sorted(md_files):
        changed, changes = process_file(file_path)
        if changed:
            total_changed += 1
            rel_path = os.path.relpath(file_path, syllabi_dir)
            all_changes[rel_path] = changes
            print(f"✓ Updated: {rel_path}")

    print("\nSummary:")
    print(f"- Total files processed: {len(md_files)}")
    print(f"- Files changed: {total_changed}")
    print(f"- Files unchanged: {len(md_files) - total_changed}")

    if all_changes:
        print("Detailed changes by file:")
        for file_path, changes in all_changes.items():
            print(f"\n{file_path}:")
            if len(set(changes)) > 10:
                print(f"  - ... and {len(set(changes)) - 10} more changes")

if __name__ == "__main__":
    main()
