from fastapi import FastAPI


from database import engine

from models import Base


from api.football_api import get_events




Base.metadata.create_all(
    bind=engine
)



app = FastAPI(
    title="MarathonIQ API"
)




@app.get("/")
def home():


    return {


        "status":
        "MarathonIQ online"

    }





@app.get("/test-api")
def test_api():


    matches = get_events()


    return {


        "count":
        len(matches),


        "first_match":

        matches[0]
        if isinstance(matches,list)
        and len(matches)>0
        else None

    }