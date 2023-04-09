from fastapi import FastAPI, Depends

# Socket.io
from api.sockets.sockets import sio_app
from fastapi.middleware.cors import CORSMiddleware

# User Schema
from api.schemas.user_schema import *
# User Controller
from api.controllers.user_controller import *

from api.utils.docs import tags_metadata


from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

# Routers
from api.routers import users_router, profile_router

app = FastAPI(openapi_tags=tags_metadata)

# -- Middleware -- #
app.add_middleware(CORSMiddleware, allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

@app.post('/token')
async def get_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    login_input = LoginDto(email=form_data.username,password=form_data.password)
    token = await login_c(db=db,login_input=login_input)
    return {
        "access_token": token,
        "token_type": "bearer"
    }

# Register Routers
app.include_router(users_router.router)
app.include_router(profile_router.router)


# Sockets
app.mount('/', app=sio_app)