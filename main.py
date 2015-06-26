import requests
import re
import json

def search(arg):
    
    # arg contains a dict with a single key:value
    # term is PO accession term and is mandatory
    
    # Validate against a regular expression
    term = arg['term']
    #term = term.upper()
    p = re.compile('[A-Z,a-z,0-9]', re.IGNORECASE)
    if not p.search(term):
       raise Exception('"term" is not valid')

    r = requests.get('http://palea.cgrb.oregonstate.edu/services/PO_web_service.php?request_type=term_search&search_value=' + term + '&inc_synonyms&branch_filter=plant_anatomy&max=20&prioritize_exact_match')
    
    #print r.headers['Content-Type']
    #print r.text
    
    r.raise_for_status()
    return r.headers['Content-Type'], r.content

def list(arg):
    pass
