from typing import List, Dict, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from Data.connection import Table
from Routers.helpers import add_badge_requests_to_applications, add_badge_request_to_requests_table

    
class Application(BaseModel):
    email: str
    RowKey: str


router = APIRouter(prefix="/api/v1/applications", tags=["applications"])


@router.post("/")
async def create_application(application: Application, badges: list):
    add_badge_request_to_requests_table(badges)
    return application
    
    
@router.get("/")
async def get_all_applications():
    applications_table = Table('applications')
    applications_dict = applications_table.query()
    raw_applications_list = applications_dict.items
    applications = add_badge_requests_to_applications(raw_applications_list)
    return applications


@router.get("/{application_id}")
async def get_application(application_id: int):
    application_table = Table("applications")
    application_data_dict = application_table.query('RowKey', f'{application_id}') # Returns generator if ID is nonexistent
    
    if len(list(application_data_dict)) == 0:
        raise HTTPException(status_code=404, detail="Application not found")
    
    raw_application_list = application_data_dict.items
    application = add_badge_requests_to_applications(raw_application_list)
    return application[0]
