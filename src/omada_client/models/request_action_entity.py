from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestActionEntity")


@_attrs_define
class RequestActionEntity:
    """List of OpenAPIs that require batch execution. Up to 20 entries are allowed for the action list

    Attributes:
        path (str): OpenAPI request path. Same as regular OpenAPI, file upload and download are not supported.
        method (str): OpenAPI request method. Same as regular OpenAPI, it should be a value as follows: POST, PATCH,
            PUT, DELETE.
        body (str | Unset): OpenAPI request body, same as regular OpenAPI. Should be a JSON object but not a string.
        query (str | Unset): OpenAPI request query of the path, same as regular OpenAPI.
    """

    path: str
    method: str
    body: str | Unset = UNSET
    query: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        method = self.method

        body = self.body

        query = self.query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "method": method,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        path = d.pop("path")

        method = d.pop("method")

        body = d.pop("body", UNSET)

        query = d.pop("query", UNSET)

        request_action_entity = cls(
            path=path,
            method=method,
            body=body,
            query=query,
        )

        request_action_entity.additional_properties = d
        return request_action_entity

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
