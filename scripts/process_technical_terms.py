#!/usr/bin/env python
"""
Script to add backticks around technical terms in markdown files.
"""
import re
from pathlib import Path

# Comprehensive list of technical terms to wrap in backticks
TECHNICAL_TERMS = {
    # Programming Languages & Versions
    'Python', 'Python 2', 'Python 3', 'Python 3.9', 'Python 3.8', 'Python 3.7', 'Python 3.6',
    'Java', 'Java 17', 'Java 11', 'Java 8', 'C', 'C++', 'C++11', 'C++14', 'C++17', 'C++20', 'C++23', 'C++98',
    'C#', 'JavaScript', 'TypeScript', 'Go', 'Rust', 'Kotlin', 'Scala', 'Ruby', 'PHP', 'Swift',
    'Objective-C', 'Perl', 'Bash', 'PowerShell', 'R', 'MATLAB', 'Fortran', 'COBOL', 'Assembly',
    'SQL', 'PL/SQL', 'T-SQL', 'ES6', 'C99', 'C17', 'C2X',

    # Frameworks & Libraries
    'React', 'Angular', 'Vue.js', 'Django', 'Flask', 'FastAPI', 'Spring', 'Spring Boot',
    'Spring Cloud', 'Hibernate', 'JPA', 'Express.js', 'Node.js', 'jQuery', 'Bootstrap',
    'Tailwind CSS', 'Material-UI', 'Redux', 'Vuex', 'RxJS', 'Lodash', 'Moment.js',
    'Chart.js', 'D3.js', 'Three.js', 'Electron', 'Cordova', 'Ionic', 'React Native',
    'Flutter', 'Xamarin', 'Unity', 'Unreal Engine', 'TensorFlow', 'PyTorch', 'Keras',
    'scikit-learn', 'NumPy', 'Pandas', 'Matplotlib', 'Seaborn', 'OpenCV', 'NLTK',
    'spaCy', 'Jupyter', 'Anaconda', 'STL',

    # Databases & Storage
    'MySQL', 'PostgreSQL', 'Oracle', 'SQL Server', 'SQLite', 'MongoDB', 'Redis',
    'Cassandra', 'DynamoDB', 'Elasticsearch', 'Neo4j', 'InfluxDB', 'CouchDB', 'MariaDB',
    'Firestore', 'Google Cloud Storage', 'Azure Blob Storage', 'HDFS',
    'Hive', 'HBase', 'Druid', 'Presto', 'Trino',

    # Cloud Platforms & Services
    'AWS', 'Azure', 'Google Cloud Platform', 'GCP', 'IBM Cloud', 'Oracle Cloud',
    'DigitalOcean', 'Heroku', 'Vercel', 'Netlify', 'CloudFlare',
    'EC2', 'S3', 'Lambda', 'RDS', 'CloudFormation', 'CloudWatch', 'API Gateway',
    'EKS', 'ECS', 'ECR', 'IAM', 'VPC', 'Route 53', 'CloudFront', 'SQS', 'SNS',
    'Amazon EC2', 'Amazon S3', 'Amazon RDS', 'Amazon DynamoDB', 'Amazon Lambda',
    'Amazon VPC', 'Amazon Route 53', 'Amazon CloudFront', 'Amazon EBS', 'Amazon EFS',
    'Amazon Glacier', 'Amazon CloudWatch', 'AWS CloudTrail', 'Amazon Machine Images',
    'AMIs', 'Elastic Load Balancing', 'ELB', 'Auto Scaling', 'FSx',
    'AWS Identity and Access Management', 'AWS Well-Architected Framework',
    'AWS Management Console', 'AWS Certified Cloud Practitioner',

    # DevOps & CI/CD Tools
    'Docker', 'Kubernetes', 'Jenkins', 'GitLab CI', 'GitHub Actions', 'Azure DevOps',
    'CircleCI', 'Travis CI', 'TeamCity', 'Bamboo', 'Ansible', 'Puppet', 'Chef',
    'Terraform', 'Helm', 'Istio', 'Linkerd', 'Prometheus', 'Grafana', 'Jaeger',
    'Zipkin', 'ELK Stack', 'Logstash', 'Kibana', 'Fluentd',
    'Consul', 'Vault', 'Nomad', 'Argo CD', 'Nexus',

    # Version Control & Collaboration
    'Git', 'GitHub', 'GitLab', 'Bitbucket', 'Subversion', 'SVN', 'Mercurial',
    'Perforce', 'Azure Repos', 'Gerrit',

    # Build Tools & Package Managers
    'Maven', 'Gradle', 'Ant', 'Make', 'CMake', 'Bazel', 'Buck', 'SBT', 'Leiningen',
    'npm', 'yarn', 'pip', 'conda', 'gem', 'composer', 'NuGet', 'CocoaPods',
    'Carthage', 'SPM', 'setuptools', 'distutils', 'virtualenv', 'PyPI', 'pydoc',

    # Testing Frameworks & Tools
    'JUnit', 'TestNG', 'Mockito', 'Selenium', 'Cypress', 'Jest', 'Mocha', 'Jasmine',
    'Karma', 'Protractor', 'Cucumber', 'Postman', 'Newman', 'SoapUI', 'JMeter',
    'Gatling', 'Locust', 'pytest', 'unittest', 'nose', 'Robot Framework', 'Appium',

    # IDEs & Editors
    'IntelliJ IDEA', 'Eclipse', 'Visual Studio', 'Visual Studio Code', 'VSCode',
    'Sublime Text', 'Atom', 'Vim', 'Emacs', 'Nano', 'WebStorm', 'PyCharm',
    'PhpStorm', 'RubyMine', 'CLion', 'GoLand', 'Rider', 'Xcode', 'Android Studio',
    'JetBrains',

    # Operating Systems & Platforms
    'Linux', 'Windows', 'macOS', 'Unix', 'Ubuntu', 'Ubuntu 22.04', 'CentOS', 'RHEL',
    'Debian', 'SUSE', 'Alpine', 'FreeBSD', 'Android', 'iOS', 'Windows Server',
    'FreeRTOS',

    # Networking & Protocols
    'HTTP', 'HTTPS', 'TCP', 'UDP', 'IP', 'DNS', 'DHCP', 'FTP', 'SFTP', 'SSH',
    'SSL', 'TLS', 'SMTP', 'IMAP', 'POP3', 'LDAP', 'SNMP', 'NFS', 'SMB',
    'WebSocket', 'gRPC', 'GraphQL', 'REST', 'SOAP', 'OAuth', 'JWT', 'SAML',

    # Data Formats & Standards
    'JSON', 'XML', 'YAML', 'CSV', 'TSV', 'Parquet', 'Avro', 'Protocol Buffers',
    'protobuf', 'MessagePack', 'TOML', 'INI', 'HTML', 'CSS', 'Markdown', 'LaTeX', 'PDF',

    # Methodologies & Practices
    'Agile', 'Scrum', 'Kanban', 'Lean', 'DevOps', 'CI/CD', 'TDD', 'BDD', 'DDD',
    'SOLID', 'Design Patterns', 'Microservices', 'Monolith', 'SOA',
    'Event-Driven Architecture', 'CQRS', 'Event Sourcing', 'OO',

    # Security & Cryptography
    'SSL/TLS', 'PKI', 'RSA', 'AES', 'SHA', 'MD5', 'OAuth 2.0', 'OpenID Connect',
    'Kerberos', 'Active Directory', 'VPN', 'IPSec', 'Firewall', 'WAF', 'IDS',
    'IPS', 'SIEM',

    # Command Line Tools & Utilities
    'grep', 'awk', 'sed', 'find', 'curl', 'wget', 'ssh', 'scp', 'rsync', 'tar',
    'zip', 'unzip', 'ps', 'top', 'htop', 'netstat', 'tcpdump', 'wireshark',
    'ping', 'traceroute', 'nslookup', 'dig', 'sudo', 'GDB',

    # File Systems & Storage
    'NTFS', 'FAT32', 'ext4', 'XFS', 'ZFS', 'Btrfs', 'APFS', 'HFS+', 'CIFS',
    'iSCSI', 'SAN', 'NAS', 'RAID', 'LVM',

    # Big Data & Analytics
    'Hadoop', 'Spark', 'Kafka', 'Storm', 'Flink', 'Pig', 'Airflow', 'Luigi',
    'Oozie', 'Zookeeper', 'Flume', 'Sqoop', 'Apache Kafka', 'Kafka Streams',
    'Apache Spark', 'Splunk',

    # Machine Learning & AI
    'XGBoost', 'LightGBM', 'CatBoost', 'H2O.ai', 'MLflow', 'Kubeflow',
    'Apache Mahout', 'Weka', 'OpenAI', 'Hugging Face', 'AI', 'Machine Learning',

    # Configuration & Web Servers
    'Apache HTTP Server', 'Apache', 'Nginx', 'IIS', 'Tomcat', 'Jetty', 'HAProxy',

    # Hardware & Architecture
    'CPU', 'GPU', 'RAM', 'SSD', 'HDD', 'ARM', 'x86', 'x64', 'RISC-V', 'FPGA',
    'ASIC', 'PCIe', 'USB', 'Ethernet', 'WiFi', 'Bluetooth',

    # General Technical Terms
    'API', 'REST API', 'Web Services', 'Dockerfile', 'Docker HUB', 'IT',
    'IDEs', 'OOP', 'IO', 'Unicode', 'UNIX', 'NoSQL', 'Cloud Computing',
    'Amazon Web Services', 'Virtual Private Cloud', 'Simple Storage Service',
    'Elastic Compute Cloud', 'Elastic Block Store', 'Elastic File System',
    'Relational Database Service', 'def', 'class', 'enumerate',
    'subprocess', 'multiprocessing', 'threading', 'int', 'float', 'str', 'bool',
    'list', 'dict', 'set', 'tuple', 'lambda', 'dir', 'print', 'if', 'while',
    'for', 'range', 'break', 'continue', 'pass', 'finally',
    'RabbitMQ', 'QEMU', 'Buildroot', 'Yocto', 'OpenCL', 'ALSA', 'NDK',
    'Web', 'fastapi',

    # HTTP Status codes and technical numbers
    '200', '404', '500', '401', '403', 'HTTP 200', 'HTTP 404', 'HTTP 500',

    # Python specific
    'pycharm', 'python'
}

def create_pattern():
    """Create regex pattern for technical terms."""
    # Sort by length (longest first) to avoid partial matches
    sorted_terms = sorted(TECHNICAL_TERMS, key=len, reverse=True)
    # Escape special regex characters and create word boundary pattern
    escaped_terms = [re.escape(term) for term in sorted_terms]
    pattern = r'\b(?:' + '|'.join(escaped_terms) + r')\b'
    return re.compile(pattern, re.IGNORECASE)

def should_skip_backticks(text, match_start, match_end):
    """Check if we should skip adding backticks around this match."""
    # Check if already in backticks
    before_start = max(0, match_start - 1)
    after_end = min(len(text), match_end + 1)

    if (before_start < len(text) and text[before_start] == '`' and
        after_end < len(text) and text[after_end] == '`'):
        return True

    # Check if inside code blocks
    before_text = text[:match_start]
    triple_backticks_before = before_text.count('```')
    if triple_backticks_before % 2 == 1:  # Inside code block
        return True

    # Check if inside inline code
    single_backticks_before = before_text.count('`')
    if single_backticks_before % 2 == 1:  # Inside inline code
        return True

    return False

def process_file(file_path):
    """Process a single markdown file to add backticks around technical terms."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    pattern = create_pattern()

    # Find all matches and their positions
    matches = []
    for match in pattern.finditer(content):
        start, end = match.span()
        if not should_skip_backticks(content, start, end):
            matches.append((start, end, match.group()))

    # Apply changes from right to left to maintain positions
    for start, end, term in reversed(matches):
        content = content[:start] + f'`{term}`' + content[end:]

    # Only write if there were changes
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False


def main():
    """Main function to process all markdown files."""
    syllabi_dir = Path("/home/mark/git/veltzer/teaching-syllabi/syllabi")

    if not syllabi_dir.exists():
        print(f"Directory {syllabi_dir} does not exist!")
        return

    # Find all markdown files
    md_files = list(syllabi_dir.rglob("*.md"))

    print(f"Found {len(md_files)} markdown files to process...")

    modified_files = []
    for file_path in md_files:
        if process_file(file_path):
            modified_files.append(str(file_path))
            print(f"Modified: {file_path}")

    print("Processing complete!")
    print(f"Modified {len(modified_files)} out of {len(md_files)} files.")

    if modified_files:
        print("\nModified files:")
        for file_path in modified_files:
            print(f"  {file_path}")

if __name__ == "__main__":
    main()
