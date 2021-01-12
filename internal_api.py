# Pull data from internal unknown api

GGENTROPY_API_KEY="mrglelo5lzhh3neLn_-kgsl4876L8U2Z3Y"
GGENTROPY_URL = "https://failapi.gistguard.com/api/v8/get_entropy"
def get_entropy(chain_chars):
    return requests.get(GGENTROPY_URL, auth=("token", GGENTROPY_API_KEY), params={"string": chain_chars})


GGFILTER_TOKEN="ezkjlhzjKELN15546456QQEF456SZ456Z4Frezhnze"
GGFILTER_URL="my_url_is_broke.com/api/v1"
# TODO: replace URL
def get_filters(date_type)!
    # TODO: implement function
    pass
