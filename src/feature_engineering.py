import pandas as pd
import re
from urllib.parse import urlparse

def get_url_length(url):
    return len(url)

def get_hostname_length(url):
    return len(urlparse(url).netloc)

def get_count_letters(url):
    return sum(c.isalpha() for c in url)

def get_count_digits(url):
    return sum(c.isdigit() for c in url)

def get_count_special_char(url, char):
    return url.count(char)

def get_count_www(url):
    return url.count('www')

def get_has_ip(url):
    # Regex for IPv4
    match = re.search(r'(([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\/)|'  # IPv4
                      r'((0x[0-9a-fA-F]{1,2})\.(0x[0-9a-fA-F]{1,2})\.(0x[0-9a-fA-F]{1,2})\.(0x[0-9a-fA-F]{1,2})\/)' # IPv4 in hexadecimal
                      r'(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url) # Ipv6
    if match:
        return 1
    else:
        return 1 if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url) else 0

def get_abnormal_url(url):
    # Heuristic: if hostname is not in url (which is weird) or maybe if whois fails (can't do here)
    # Let's use a simple heuristic: if the URL has no hostname
    hostname = urlparse(url).netloc
    if hostname:
        return 0
    return 1

def get_short_url(url):
    shortening_services = r'bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|' \
                          r'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|' \
                          r'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|' \
                          r'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|' \
                          r'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|' \
                          r'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|' \
                          r'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|' \
                          r'tr\.im|link\.zip\.net'
    match = re.search(shortening_services, url, flags=re.IGNORECASE)
    return 1 if match else 0

def get_https(url):
    return 1 if urlparse(url).scheme == 'https' else 0

def get_count_dir(url):
    path = urlparse(url).path
    return path.count('/')

def get_count_embed_domain(url):
    return max(0, url.count('http') - 1)

def get_fd_length(url):
    path = urlparse(url).path
    try:
        return len(path.split('/')[1])
    except IndexError:
        return 0

def get_tld_length(url):
    try:
        return len(urlparse(url).netloc.split('.')[-1])
    except:
        return 0

def get_suspicious(url):
    keywords = ['login', 'update', 'free', 'paypal', 'secure', 'account', 'banking', 'confirm', 'signin', 'verify']
    return 1 if any(keyword in url.lower() for keyword in keywords) else 0

def extract_features(df):
    """
    Extract features from the 'url' column of the dataframe.
    
    Args:
        df (pd.DataFrame): Dataframe containing 'url' column.
        
    Returns:
        pd.DataFrame: Dataframe with new features.
    """
    df = df.copy()
    
    print("Extracting features... This may take a moment.")
    df['url_length'] = df['url'].apply(get_url_length)
    df['hostname_length'] = df['url'].apply(get_hostname_length)
    df['count_letters'] = df['url'].apply(get_count_letters)
    df['count_digits'] = df['url'].apply(get_count_digits)
    df['count_@'] = df['url'].apply(lambda x: get_count_special_char(x, '@'))
    df['count_?'] = df['url'].apply(lambda x: get_count_special_char(x, '?'))
    df['count_-'] = df['url'].apply(lambda x: get_count_special_char(x, '-'))
    df['count_='] = df['url'].apply(lambda x: get_count_special_char(x, '='))
    df['count_.'] = df['url'].apply(lambda x: get_count_special_char(x, '.'))
    df['count_#'] = df['url'].apply(lambda x: get_count_special_char(x, '#'))
    df['count_%'] = df['url'].apply(lambda x: get_count_special_char(x, '%'))
    df['count_+'] = df['url'].apply(lambda x: get_count_special_char(x, '+'))
    df['count_$'] = df['url'].apply(lambda x: get_count_special_char(x, '$'))
    df['count_!'] = df['url'].apply(lambda x: get_count_special_char(x, '!'))
    df['count_*'] = df['url'].apply(lambda x: get_count_special_char(x, '*'))
    df['count_,'] = df['url'].apply(lambda x: get_count_special_char(x, ','))
    df['count_slashes'] = df['url'].apply(lambda x: get_count_special_char(x, '/'))
    df['count_www'] = df['url'].apply(get_count_www)
    df['has_ip'] = df['url'].apply(get_has_ip)
    df['abnormal_url'] = df['url'].apply(get_abnormal_url)
    df['short_url'] = df['url'].apply(get_short_url)
    df['https'] = df['url'].apply(get_https)
    df['count_dir'] = df['url'].apply(get_count_dir)
    df['count_embed_domain'] = df['url'].apply(get_count_embed_domain)
    df['fd_length'] = df['url'].apply(get_fd_length)
    df['tld_length'] = df['url'].apply(get_tld_length)
    df['suspicious'] = df['url'].apply(get_suspicious)
    
    print("Feature extraction complete.")
    return df
