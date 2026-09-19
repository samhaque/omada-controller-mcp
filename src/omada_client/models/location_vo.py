from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationVO")


@_attrs_define
class LocationVO:
    """Device location information on the map; null indicates unplaced.

    Attributes:
        locked (bool | Unset): Whether is locked
        map_id (str | Unset): Map id
        pos_x (float | Unset): X-axis position
        pos_y (float | Unset): Y-axis position
        install_type (int | Unset): The installation method affects the default mounting height: CEILING (0), DESK (1),
            PANEL (2), WALL (3), POLE (4).
        height (float | Unset): Height
        angle (int | Unset): Angle
        located (bool | Unset): Whether the device is located,false: indicates the disassociation of the device from the
            map.
    """

    locked: bool | Unset = UNSET
    map_id: str | Unset = UNSET
    pos_x: float | Unset = UNSET
    pos_y: float | Unset = UNSET
    install_type: int | Unset = UNSET
    height: float | Unset = UNSET
    angle: int | Unset = UNSET
    located: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locked = self.locked

        map_id = self.map_id

        pos_x = self.pos_x

        pos_y = self.pos_y

        install_type = self.install_type

        height = self.height

        angle = self.angle

        located = self.located

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locked is not UNSET:
            field_dict["locked"] = locked
        if map_id is not UNSET:
            field_dict["mapId"] = map_id
        if pos_x is not UNSET:
            field_dict["posX"] = pos_x
        if pos_y is not UNSET:
            field_dict["posY"] = pos_y
        if install_type is not UNSET:
            field_dict["installType"] = install_type
        if height is not UNSET:
            field_dict["height"] = height
        if angle is not UNSET:
            field_dict["angle"] = angle
        if located is not UNSET:
            field_dict["located"] = located

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        locked = d.pop("locked", UNSET)

        map_id = d.pop("mapId", UNSET)

        pos_x = d.pop("posX", UNSET)

        pos_y = d.pop("posY", UNSET)

        install_type = d.pop("installType", UNSET)

        height = d.pop("height", UNSET)

        angle = d.pop("angle", UNSET)

        located = d.pop("located", UNSET)

        location_vo = cls(
            locked=locked,
            map_id=map_id,
            pos_x=pos_x,
            pos_y=pos_y,
            install_type=install_type,
            height=height,
            angle=angle,
            located=located,
        )

        location_vo.additional_properties = d
        return location_vo

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
