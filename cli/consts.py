PRE_COMMIT_SCAN_COMMAND_TYPE = 'pre_commit'

SECRET_SCAN_TYPE = 'secret'
INFRA_CONFIGURATION_SCAN_TYPE = 'iac'
SCA_SCAN_TYPE = "sca"

INFRA_CONFIGURATION_SCAN_SUPPORTED_FILES = [
    '.tf', '.tf.json', '.json', '.yaml', '.yml', 'dockerfile'
]

SECRET_SCAN_FILE_EXTENSIONS_TO_IGNORE = [
    '.7z', '.bmp', '.bz2', '.dmg', '.exe', '.gif', '.gz', '.ico', '.jar', '.jpg', '.jpeg', '.png', '.rar',
    '.realm', '.s7z', '.svg', '.tar', '.tif', '.tiff', '.webp', '.zi', '.lock', '.css', '.less', '.dll',
    '.enc', '.deb', '.obj', '.model'
]

SCA_CONFIGURATION_SCAN_SUPPORTED_FILES = [
    'cargo.lock', 'cargo.toml',
    'composer.json', 'composer.lock',
    'go.sum', 'go.mod', 'gopkg.lock',
    'pom.xml', 'build.gradle', 'gradle.lockfile', 'build.gradle.kts',
    'package.json', 'package-lock.json', 'yarn.lock', 'npm-shrinkwrap.json',
    'packages.config', 'project.assets.json', 'packages.lock.json', 'nuget.config', '.csproj',
    'gemfile', 'gemfile.lock',
    'build.sbt', 'build.scala', 'build.sbt.lock',
    'pyproject.toml', 'poetry.lock',
    'pipfile', 'pipfile.lock', 'requirements.txt', 'setup.py'
]

PROJECT_FILES_BY_ECOSYSTEM_MAP = {
    "crates": ["Cargo.lock", "Cargo.toml"],
    "composer": ["composer.json", "composer.lock"],
    "go": ["go.sum", "go.mod", "Gopkg.lock"],
    "maven_pom": ["pom.xml"],
    "maven_gradle": ["build.gradle", "build.gradle.kts", "gradle.lockfile"],
    "npm": ["package.json", "package-lock.json", "yarn.lock", "npm-shrinkwrap.json", ".npmrc"],
    "nuget": ["packages.config", "project.assets.json", "packages.lock.json", "nuget.config"],
    "ruby_gems": ["Gemfile", "Gemfile.lock"],
    "sbt": ["build.sbt", "build.scala", "build.sbt.lock"],
    "pypi_poetry": ["pyproject.toml", "poetry.lock"],
    "pypi_pipenv": ["Pipfile", "Pipfile.lock"],
    "pypi_requirements": ["requirements.txt"],
    "pypi_setup": ["setup.py"]
}

COMMIT_RANGE_SCAN_SUPPORTED_SCAN_TYPES = [SECRET_SCAN_TYPE, SCA_SCAN_TYPE]

DEFAULT_CYCODE_API_URL = "https://api.cycode.com"
DEFAULT_CYCODE_APP_URL = "https://app.cycode.com"

# env var names
CYCODE_API_URL_ENV_VAR_NAME = "CYCODE_API_URL"
CYCODE_APP_URL_ENV_VAR_NAME = "CYCODE_APP_URL"
TIMEOUT_ENV_VAR_NAME = "TIMEOUT"
CYCODE_CLI_REQUEST_TIMEOUT_ENV_VAR_NAME = "CYCODE_CLI_REQUEST_TIMEOUT"
LOGGING_LEVEL_ENV_VAR_NAME = "LOGGING_LEVEL"
# use only for dev envs locally
DEV_MODE_ENV_VAR_NAME = "DEV_MODE"
BATCH_SIZE_ENV_VAR_NAME = "BATCH_SIZE"
VERBOSE_ENV_VAR_NAME = "CYCODE_CLI_VERBOSE"

CYCODE_CONFIGURATION_DIRECTORY: str = '.cycode'

# user configuration sections names
EXCLUSIONS_BY_VALUE_SECTION_NAME = 'values'
EXCLUSIONS_BY_SHA_SECTION_NAME = 'shas'
EXCLUSIONS_BY_PATH_SECTION_NAME = 'paths'
EXCLUSIONS_BY_RULE_SECTION_NAME = 'rules'
EXCLUSIONS_BY_PACKAGE_SECTION_NAME = 'packages'

# 1MB in bytes (in decimal)
FILE_MAX_SIZE_LIMIT_IN_BYTES = 1000000

# 10MB in bytes (in binary)
ZIP_MAX_SIZE_LIMIT_IN_BYTES = 10485760
# 200MB in bytes (in binary)
SCA_ZIP_MAX_SIZE_LIMIT_IN_BYTES = 209715200

# scan with polling
SCAN_POLLING_WAIT_INTERVAL_IN_SECONDS = 10
SCAN_POLLING_TIMEOUT_IN_SECONDS_DEFAULT = 3600
SCAN_POLLING_TIMEOUT_IN_SECONDS_ENV_VAR_NAME = 'SCAN_POLLING_TIMEOUT_IN_SECONDS'
DETECTIONS_COUNT_VERIFICATION_TIMEOUT_IN_SECONDS = 600
DETECTIONS_COUNT_VERIFICATION_WAIT_INTERVAL_IN_SECONDS = 10
SCA_PRE_COMMIT_TIMEOUT_IN_SECONDS_DEFAULT = 600
SCA_PRE_COMMIT_TIMEOUT_IN_SECONDS_ENV_VAR_NAME = 'SCA_PRE_COMMIT_TIMEOUT_IN_SECONDS'

# scan statuses
SCAN_STATUS_COMPLETED = 'Completed'
SCAN_STATUS_ERROR = 'Error'

# git consts
COMMIT_DIFF_DELETED_FILE_CHANGE_TYPE = 'D'
GIT_HEAD_COMMIT_REV = 'HEAD'
