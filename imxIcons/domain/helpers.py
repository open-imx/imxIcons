from imxIcons.iconEntity import IconEntity


def copy_icon_and_assign_imx_path(
    imx_path: str, icon_entities: list[IconEntity]
) -> list[IconEntity]:
    new_icon_entities = []
    for icon in icon_entities:
        icon_copy = icon.extend_icon(icon.icon_name, extra_props={}, extra_groups=[])
        icon_copy.imx_path = imx_path
        new_icon_entities.append(icon_copy)
    return new_icon_entities
