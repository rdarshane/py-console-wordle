import json
import requests

class dictionary_service:

    @classmethod
    def get_word(cls, word_id):
        app_id  = "bdcaaaea"#"XXX enter app-id here"
        app_key  = "4b969b3059b9cf15406310c1b8d214c3"#"XXX enter API key here"
        endpoint = "entries"
        language_code = "en-us"        
        url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
        r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
        return (r.status_code == 200, r.text)