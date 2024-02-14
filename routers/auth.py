from fastapi import APIRouter, HTTPException, Depends
from passlib.hash import pbkdf2_sha256
from pydantic import BaseModel, Field
from starlette import status
from datetime import timedelta, datetime
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from controllers.authenticate import Authenticate
from controllers.user import User

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY = 'e9a1595b6c9b50d3d0ba4f1e73241c0d1bc8f3d6e19820cda48245fc5c607cdc'
ALGORITHM = 'HS256'

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class UserModel(BaseModel):
    unique_id: str = Field(min_length=3)
    security_code: str = Field(min_length=8)
    account_number: str = Field(min_length=10)
    name: str = Field(max_length=25)
    balance: str = Field(min_length=1)
    account_type: str = Field(min_length=2, max_length=12)

class AuthModel(BaseModel):
    unique_id: str = Field(min_length=3)
    security_code: str = Field(min_length=8)
   
class Token(BaseModel):
    access_token: str
    token_type: str
    
    
def create_access_token(unique_id: str, user_role:str, expires_delta: timedelta):
    encode = {'id': unique_id, 'role': user_role}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
       
    
@router.post("/login", status_code=status.HTTP_200_OK, response_model = Token)
async def login_for_access_token(auth_data: AuthModel):
    auth_details = {
        "unique_id": auth_data.unique_id,
        "security_code": auth_data.security_code
    }
    user = Authenticate( unique_id = auth_data.unique_id,
        security_code  = auth_data.security_code)
    logged = user.check_credentials()
    if logged:
        token = create_access_token(auth_data.unique_id, 'admin', timedelta(minutes=20))
        return {'access_token': token, 'token_type': 'bearer'}
    else:
        raise HTTPException(404, detail="User not found")
    
    
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_id: str = payload.get('user_id')
        role: str = payload.get('role')
        if user_id is None:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')

        return {'user_id': user_id, 'role': role}
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')
    

# user_dependency = Annotated[dict, Depends(get_current_user)]


   

# def authenticate_user(unique_id, security_code):
#     auth = Authenticate(unique_id, security_code)
#     db_password = auth.check_credentials()
#     if db_password and pbkdf2_sha256.verify(unique_id, security_code):
#         return True
#     return False


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def add_user(user_data: UserModel):
    user = User(
        unique_id = user_data["unique_id"],
        security_code = pbkdf2_sha256.hash(user_data.security_code),       
        account_number = user_data["account_number"],
        name = user_data["name"],
        balance = user_data["balance"],
        account_type = user_data["account_type"],
        )
    if user.add_customer():
        return user
    else:
        raise HTTPException(status_code=422, detail='Cannot add user')




# @router.post("/token", status_code=status.HTTP_200_OK, response_model = Token)
# async def login_for_access_token(auth_data: AuthModel):
#     user = authenticate_user(auth_data.unique_id, auth_data.security_code)
#     if not user:
#         return 'Failed Authentication'

#     token = create_access_token(auth_data.unique_id, timedelta(minutes=20))
#     return {'access_token': token, 'token_type': 'bearer'}

# form_data: Annotated[OAuth2PasswordRequestForm, DeprecationWarning]