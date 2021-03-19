from typing import List, Dict, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from Data.connection import Table
from Routers.helpers import (add_badge_requests_to_applications, add_badge_request_to_requests_table, 
                             delete_badge_requests_from_requests_table)


router = APIRouter(prefix="/api/v1/applications", tags=["applications"])


class Application(BaseModel):
    PartitionKey: str
    RowKey: str
    requests: List[dict]


@router.post("/")
async def create_application(application: Application):
    add_badge_request_to_requests_table(application.requests)
    applications_table = Table('applications')
    application_dict = dict(PartitionKey=application.PartitionKey, RowKey=application.RowKey)
    applications_table.insert(application_dict)
    return application


@router.delete("/{application_id}")
async def delete_application(application_id: str):
    delete_badge_requests_from_requests_table(application_id)
    applications_table = Table('applications')
    application_data_generator = applications_table.query("RowKey", application_id)
    application_data = list(application_data_generator)[0]
    applications_table.delete(partition_key=application_data.PartitionKey, row_key=application_data.RowKey)
    return {"Details": "Application deleted"}
    
    
@router.get("/")
async def get_all_applications():
    applications_table = Table('applications')
    applications_dict = applications_table.query()
    raw_applications_list = applications_dict.items
    applications = add_badge_requests_to_applications(raw_applications_list)
    return applications


@router.get("/{application_id}")
async def get_application(application_id: str):
    application_table = Table("applications")
    application_data_dict = application_table.query('RowKey', application_id)
    
    if len(list(application_data_dict)) == 0:
        raise HTTPException(status_code=404, detail="Application not found")
    
    raw_application_list = application_data_dict.items
    application = add_badge_requests_to_applications(raw_application_list)
    return application[0]
