from os import path
from os import environ

APP_DIR = path.dirname(path.dirname(path.realpath(__file__)))
SKIN_DIR = path.join(APP_DIR, "view")
TEMPLATES_DIR = path.join(SKIN_DIR, "templates")
STATIC_DIR = path.join(SKIN_DIR, "style")
LOGFILE = APP_DIR + "/flask.log"
VOCAB_CACHE_DIR = path.join(APP_DIR, "cache")
VOCAB_CACHE_HOURS = (
    1  # Number of hours before cache is replaced (set to zero to always replace)
)
DEFAULT_LANGUAGE = "en"
SPARQL_QUERY_LIMIT = 2000  # Maximum number of results to return per SPARQL query
MAX_RETRIES = 2
RETRY_SLEEP_SECONDS = 10
SPARQL_TIMEOUT = 60
LOCAL_URLS = False  # Parameter governing whether URLs shown are local or external


#
#   Vocabulary data sources
#
# Here is the list of vocabulary sources that this instance uses. FILE, SPARQL, RVA & VOCBENCH are implemented already
# and are on by default (e.g. VOCBENCH = None) but other sources, such as GitHub can be added. To enable them, add a new
# like like VocBench.XXX = None
class VocabSource:
    FILE = "FILE"
    SPARQL = "SPARQL"
    RVA = "RVA"
    VOCBENCH = "VOCBENCH"
    GITHUB = "GITHUB"

# Main cache (SPARQL DB) variables
# BEGIN Instance Vars
DEBUG = True
SPARQL_ENDPOINT = environ.get("SPARQL_ENDPOINT", "http://localhost:7200/repositories/ggic-vocabs")
SPARQL_USERNAME = environ.get("SPARQL_USERNAME", "")
SPARQL_PASSWORD = environ.get("SPARQL_PASSWORD", "")
SOURCE_NAME = "ga"
# END Instance Vars

VOCAB_SOURCES = {
    # example SPARQL source configured using varaibles in "Instance Vars" above
    SOURCE_NAME: {
        "source": VocabSource.SPARQL,
        "sparql_endpoint": SPARQL_ENDPOINT,
        "sparql_username": SPARQL_USERNAME,
        "sparql_password": SPARQL_PASSWORD,
    },
}

# Details for the main vocabulary list. Can be overriden in the vocabularies.html template
# BEGIN Vocabs list info
VOCS_TITLE = "GGIC Vocabularies"
VOCS_URI = "http://ggic.vocabs.ga.gov.au"
VOCS_DESC = "Vocabularies managed and published by Geoscience Australia on behalf of the Government Geoscience Information Committee (GGIC)"
# END Vocabs list info