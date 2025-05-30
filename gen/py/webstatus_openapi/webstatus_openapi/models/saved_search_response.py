# coding: utf-8

"""
    webstatus.dev API

    A tool to monitor and track the status of all Web Platform features across dimensions that are related to availability and implementation quality across browsers, and adoption by web developers. 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SavedSearchResponse(BaseModel):
    """
    SavedSearchResponse
    """ # noqa: E501
    id: StrictStr
    updated_at: Optional[datetime] = None
    created_at: datetime
    name: StrictStr
    query: StrictStr
    subscription_status: Optional[StrictStr] = Field(default=None, description="The subscription status for a saved search for a user. This field is only populated when the request is authenticated. ")
    owner_status: Optional[StrictStr] = Field(default=None, description="The owner status for a saved search for a user. This field is only populated when the request is authenticated. ")
    __properties: ClassVar[List[str]] = ["id", "updated_at", "created_at", "name", "query", "subscription_status", "owner_status"]

    @field_validator('subscription_status')
    def subscription_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'active']):
            raise ValueError("must be one of enum values ('none', 'active')")
        return value

    @field_validator('owner_status')
    def owner_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'admin']):
            raise ValueError("must be one of enum values ('none', 'admin')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SavedSearchResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SavedSearchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "name": obj.get("name"),
            "query": obj.get("query"),
            "subscription_status": obj.get("subscription_status"),
            "owner_status": obj.get("owner_status")
        })
        return _obj


