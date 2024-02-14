from fastapi import APIRouter, HTTPException
from passlib.hash import pbkdf2_sha256
from pydantic import BaseModel, Field
from starlette import status
from controllers.account import Account
from controllers.user import User
# from models import db



router = APIRouter()


class UserModel(BaseModel):
    unique_id: str = Field(min_length=4)
    security_code: str = Field(min_length=8)
    account_number: str = Field(min_length=10)
    name: str = Field(max_length=25)
    balance: str = Field(min_length=1)
    account_type: str = Field(min_length=2, max_length=12)
    
class UniqueidModel(BaseModel):
    unique_id: str =Field(min_length=4)
    
@router.get("/balance",status_code=status.HTTP_200_OK)
async def view_balance():
    acc = Account(unique_id="7")
    result = acc.view_balance()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail='Cannot view balance')

@router.put("/deposit", status_code=status.HTTP_200_OK)
async def deposit_money(id: UniqueidModel):
    acc = Account(id)
    if acc.deposit_money("20000"):
        return "Successful"
    else:
        raise HTTPException(status_code=422, detail='Cannot deposit money')

@router.put("/withdraw", status_code=status.HTTP_200_OK)
async def withdraw_money(id: UniqueidModel):
    acc = Account(id)
    if acc.withdraw_money("20000"):
        return "Successful"
    else:
        raise HTTPException(status_code=422, detail='Cannot withdraw money')
        
        

# @router.post("/user", status_code=status.HTTP_201_CREATED)
# async def add_user(user_data: UserModel):
#     user = User(
#         unique_id = user_data.unique_id,
#         security_code = pbkdf2_sha256.hash(user_data.security_code),       
#         account_number = user_data.account_number,
#         name = user_data.name,
#         balance = user_data.balance,
#         account_type = user_data.account_type,
#         )
#     if user.add_customer():
#         return user
#     else:
#         raise HTTPException(status_code=422, detail='Cannot deposit money')
        

# @router.delete("/user")
# async def delete_user(id: UniqueidModel):
#     user = User(id)
#     if user.remove_customer():
#         return user
#     else:
#         raise HTTPException(status_code=422, detail='Cannot deposit money')
