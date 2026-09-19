from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.notification_configuration_open_api_vo_event_category import (
        NotificationConfigurationOpenApiVOEventCategory,
    )
    from ..models.notification_configuration_open_api_vo_event_level import (
        NotificationConfigurationOpenApiVOEventLevel,
    )
    from ..models.notification_configuration_open_api_vo_event_object_type import (
        NotificationConfigurationOpenApiVOEventObjectType,
    )


T = TypeVar("T", bound="NotificationConfigurationOpenApiVO")


@_attrs_define
class NotificationConfigurationOpenApiVO:
    """Email Alerts List(This config applies to the Abnormal > Notification view).

    Attributes:
        event_level (NotificationConfigurationOpenApiVOEventLevel): The incident level of event map. Key is event level,
            such as: critical, error, warning, info. Value is true or false, indicating whether the event level is selected.
        event_object_type (NotificationConfigurationOpenApiVOEventObjectType): The incident object of event. Key is
            event object type, such as: gateway, switch, ap, wiredClient, wirelessClient. Value is true or false, indicating
            whether the event object type is selected.
        event_category (NotificationConfigurationOpenApiVOEventCategory): For the values of event category Key, refer to
            section 5.7.1.1 of the Open API Access. Example: networking.
    """

    event_level: NotificationConfigurationOpenApiVOEventLevel
    event_object_type: NotificationConfigurationOpenApiVOEventObjectType
    event_category: NotificationConfigurationOpenApiVOEventCategory
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_level = self.event_level.to_dict()

        event_object_type = self.event_object_type.to_dict()

        event_category = self.event_category.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventLevel": event_level,
                "eventObjectType": event_object_type,
                "eventCategory": event_category,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.notification_configuration_open_api_vo_event_category import (
            NotificationConfigurationOpenApiVOEventCategory,
        )
        from ..models.notification_configuration_open_api_vo_event_level import (
            NotificationConfigurationOpenApiVOEventLevel,
        )
        from ..models.notification_configuration_open_api_vo_event_object_type import (
            NotificationConfigurationOpenApiVOEventObjectType,
        )

        d = dict(src_dict)
        event_level = NotificationConfigurationOpenApiVOEventLevel.from_dict(
            d.pop("eventLevel")
        )

        event_object_type = NotificationConfigurationOpenApiVOEventObjectType.from_dict(
            d.pop("eventObjectType")
        )

        event_category = NotificationConfigurationOpenApiVOEventCategory.from_dict(
            d.pop("eventCategory")
        )

        notification_configuration_open_api_vo = cls(
            event_level=event_level,
            event_object_type=event_object_type,
            event_category=event_category,
        )

        notification_configuration_open_api_vo.additional_properties = d
        return notification_configuration_open_api_vo

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
