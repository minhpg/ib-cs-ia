from fastapi import APIRouter, Request


router = APIRouter(
 prefix="/api",
)


@router.middleware("http")
async def verifyAuthorization(request: Request, call_next):

    response = await call_next(request)
    return response

