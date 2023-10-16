from fastapi import APIRouter
from app.Util import convertStruct
from app.Exceptions import APIException
from app.core.jhu import JHU
from app.Models.world_m import GlobalModel
from app.Models.exception import BaseExceptionToJsonModel

breaches= APIRouter()


@breaches.get("/search/{domain}", response_model=GlobalModel, responses={422: {"model": BaseExceptionToJsonModel}})
async def start_search(domain: str):
    """There is a difference of 2 days in the data obtained from JHU CSSE COVID-19 Data."""
    jhu = JHU()
    source = await jhu.fetch_country_status(domain)
    if source is None:
        raise APIException(
            status=False,
            system={
                "message": f"The country with alpha_3: {domain} does not exist in database",
                "code": 422
            },
            source=None

        )
    return await convertStruct(
        status=True,
        code=200,
        message="Success",
        source=source
    )
