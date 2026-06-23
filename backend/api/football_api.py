import requests

from datetime import datetime

from config import APIFOOTBALL_KEY



BASE_URL = "https://apiv3.apifootball.com/"




def get_events():


    today = datetime.now().strftime(
        "%Y-%m-%d"
    )


    params = {


        "action":
        "get_events",


        "APIkey":
        APIFOOTBALL_KEY,


        "from":
        today,


        "to":
        today

    }



    response = requests.get(

        BASE_URL,

        params=params,

        timeout=20

    )



    data = response.json()



    return data