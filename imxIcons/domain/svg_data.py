import xml.etree.ElementTree as ET


def create_fill_color(hex_color, qgis_parameter=True):
    if qgis_parameter:
        return f'fill="param(fill) {hex_color}"'
    else:
        return f'fill="{hex_color}"'


def create_stroke_color(hex_color, qgis_parameter=True):
    if qgis_parameter:
        return f'stroke="param(fill) {hex_color}"'
    else:
        return f'stroke="{hex_color}"'


def create_stroke_width(units, qgis_parameter=True):
    if qgis_parameter:
        return f'stroke-width="param(outline-width) {units}"'
    else:
        return f'stroke-width="{round(units * 0.75, 3)}"'


class IconStyleEnum:
    primary_color = "black"
    primary_stroke_width = 0.5

    secondary_color = "black"
    secondary_stroke_width = 0.3

    black = "#000000"
    white = "#FFFFFF"
    gray = "#bcbcbc"
    green = "green"
    red = "red"
    gold = "gold"
    blue = "#3a61b4"


class IconStyleDarkEnum:
    primary_color = "gray"
    primary_stroke_width = 0.5

    secondary_color = "gray"
    secondary_stroke_width = 0.3

    black = "#000000"
    white = "#FFFFFF"
    gray = "#bcbcbc"
    green = "green"
    red = "red"
    gold = "gold"
    blue = "#3a61b4"


def create_primary_icon_style(qgis=True, dark_mode=False):
    if dark_mode:
        return f"{create_fill_color(IconStyleDarkEnum.primary_color, qgis)} {create_stroke_color(IconStyleDarkEnum.primary_color, qgis)} {create_stroke_width(IconStyleDarkEnum.primary_stroke_width, qgis)}"
    return f"{create_fill_color(IconStyleEnum.primary_color, qgis)} {create_stroke_color(IconStyleEnum.primary_color, qgis)} {create_stroke_width(IconStyleEnum.primary_stroke_width, qgis)}"


def create_secondary_icon_style(qgis=True, dark_mode=False):
    if dark_mode:
        return f"{create_fill_color(IconStyleDarkEnum.secondary_color, qgis)} {create_stroke_color(IconStyleDarkEnum.secondary_color, qgis)} {create_stroke_width(IconStyleDarkEnum.secondary_stroke_width, qgis)}"
    return f"{create_fill_color(IconStyleEnum.secondary_color, qgis)} {create_stroke_color(IconStyleEnum.secondary_color, qgis)} {create_stroke_width(IconStyleEnum.secondary_stroke_width, qgis)}"


def get_svg_groups(
    qgis_render: bool = False, dark_mode: bool = False
) -> dict[str, str] | dict:
    svg_data = f"""

    <g name="insertion-point" {create_primary_icon_style(qgis_render, dark_mode)} >
        <circle r="0.15" cx="0" cy="0" fill="rgb(168, 168, 168)" />
      <polyline points="-1 0 1 0" style="stroke-width: 0.15px; stroke: rgb(168, 168, 168);" />
      <polyline points="0 -1 0 1" style="stroke-width: 0.15px; stroke: rgb(168, 168, 168);" />
    </g>

    <!-- Signal -->
    <g name="post-ground" {create_primary_icon_style(qgis_render, dark_mode)} >
        <line x1="0" x2="0" y1="-1.5" y2="1.5" />
    </g>

    <g name="signal-post-high" {create_primary_icon_style(qgis_render, dark_mode)} >
        <line x1="8.5" x2="0" y1="-0" y2="-0" />    
    </g>

    <g name="signal-post-low" {create_primary_icon_style(qgis_render, dark_mode)} >
        <line x1="0" x2="2.5" y1="-0" y2="-0" />
    </g>

    <g name="signal-aspect" class="animated" {create_primary_icon_style(qgis_render, dark_mode)} >
        <circle class="aspect-3-colors" cx="0" cy="0" r="1.5" fill="{IconStyleEnum.gold}" />
    </g>

    <g name="signal-distance" class="animated" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path class="aspect-2-colors" d="M 8.5 1.5 L 11.5 1.5 L 11.5 -1.5 L 8.5 -1.5 L 8.5 1.5" fill="{IconStyleEnum.white}" />
    </g>

    <g name="repeat" class="animated" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path class="aspect-on-off" d="M 6 2 L 10 2 L 10 -2 L 6 -2 L 6 2" fill="{IconStyleEnum.white}" />
        <line x1="7" x2="7" y1="-1" y2="1" stroke="black" />
        <line x1="9.5" x2="7.5" y1="1" y2="-1" stroke="black" />
    </g>

    <g name="departure" {create_primary_icon_style(qgis_render, dark_mode)}>
        <circle cx="0" cy="-0" r="2" fill="none"/>
        <line x1="-1.375" x2="1.375" y1="1.375" y2="-1.375"/>
        <line x1="1.375" x2="-1.375" y1="1.375" y2="-1.375"/>
    </g>

    <g name="departure-single" {create_primary_icon_style(qgis_render, dark_mode)}>
        <line x1="-4" x2="2.85" y1="-4" y2="-4"/>
        <path d="M 1.875 -4.5 L 1.875 -3.5 L 3.875 -4 L 1.875 -4.5"/>
    </g>

    <g name="departure-double" {create_primary_icon_style(qgis_render, dark_mode)}>  
        <line x1="-2.851" x2="2.688" y1="-4" y2="-4"/>
        <path d="M -2 -3.5 L -2 -4.5 L -4 -4 L -2 -3.5"/>
        <path d="M 2 -4.5 L 4 -4 L 2 -3.5 L 2 -4.5"/>
    </g>

    <g name="signal-cargo" class="animated" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path class="aspect-on-off" d="M 6 2 L 10 2 L 10 -2 L 6 -2 L 6 2" fill="{IconStyleEnum.white}" />
        <line x1="9.25" x2="6.75" y1="-0.563" y2="-0.563"  stroke="{IconStyleEnum.black}" />
        <line x1="9.25" x2="6.75" y1="0.686" y2="0.686" stroke="{IconStyleEnum.black}" />
        <line x1="8.125" x2="8.125" y1="-0.563" y2="0.686"  stroke="{IconStyleEnum.black}" />
    </g>

    <g name="signal-distant-cargo" class="animated" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path class="aspect-on-off" d="M 6 2 L 10 2 L 10 -2 L 6 -2 L 6 2" fill="{IconStyleEnum.white}" />
        <line x1="7.1" x2="7.1" y1="0.499" y2="-0.4" />
        <line x1="7.1" x2="9" y1="-0.4" y2="-0.4" />
    </g>

    <!-- Signal.IlluminatedSign -->
    <g name="illuminated-sign-integrated" class="animated" {create_primary_icon_style(qgis_render, dark_mode)} >
        <circle class="aspect-on-off" cx="0" cy="0" r="1.05" fill="{IconStyleEnum.gold}" />
        <line x1="-0.75" x2="0.75" y1="-0.75" y2="0.75" />
        <line x1="0.75" x2="-0.75" y1="-0.75" y2="0.75" />
    </g>

    <g name="illuminated-sign-not-integrated" class="animated" {create_primary_icon_style(qgis_render, dark_mode)} >
        <line x1="0" x2="0" y1="-0.5" y2="0.5" />
        <line x1="0" x2="3" y1="-0" y2="-0" />
        <rect x="2.75" y="-1" width="2.5" height="2" />
        <circle class="aspect-on-off" cx="4" cy="0" r="1" fill="{IconStyleEnum.gold}" />
        <line x1="3" y1="1" x2="5" y2="-1" />
        <line x1="3" y1="-1" x2="5" y2="1" />
    </g>

    <!-- Signal.ReflectorPost -->
    <g name="signal-reflector-straight" {create_primary_icon_style(qgis_render, dark_mode)} >
        <line x1="-4" x2="-1" y1="-1" y2="-1" /> 
        <line x1="-4" x2="-1" y1="-0" y2="-0" />
        <line x1="-4" x2="-1" y1="1" y2="1" />
    </g>

    <g name="signal-reflector-diagonal" {create_primary_icon_style(qgis_render, dark_mode)} >
        <line x1="-3.875" x2="-2.875" y1="-1" y2="1" />
        <line x1="-3" x2="-2" y1="-1" y2="1" />
        <line x1="-2.125" x2="-1.125" y1="-1" y2="1" />
    </g>

    <g name="signal-level-crossing" {create_primary_icon_style(qgis_render, dark_mode)} >
      <rect x="-1.342" y="-3.653" width="2.686" height="4.936" rx="1.309" ry="1.309" />
      <circle class="aspect-2-colors" r="0.892" cx="0" cy="0" fill="{IconStyleEnum.gold}" />
      <circle class="aspect-2-colors" cy="-2.528" r="0.892" cx="0" fill="{IconStyleEnum.gold}" />
    </g>

    <!-- symbol stamp by attributes--> 

    <g name="signal-p" {create_primary_icon_style(qgis_render, dark_mode)} >
      <path d="M -0.821 -1.092 L -0.821 -0.368 L -1.294 -0.368 L -1.294 -2.469 L -0.553 -2.469 C -0.023 -2.469 0.241 -2.246 0.241 -1.799 C 0.241 -1.588 0.166 -1.418 0.014 -1.287 C -0.138 -1.157 -0.341 -1.092 -0.595 -1.092 L -0.821 -1.092 Z M -0.821 -2.105 L -0.821 -1.451 L -0.635 -1.451 C -0.383 -1.451 -0.257 -1.561 -0.257 -1.782 C -0.257 -1.997 -0.383 -2.105 -0.635 -2.105 L -0.821 -2.105 Z" stroke-width="0.1"/>
    </g>

    <g name="signal-a" {create_primary_icon_style(qgis_render, dark_mode)} >
      <path d="M 0.624 -0.414 L 0.109 -0.414 L -0.041 -0.881 L -0.788 -0.881 L -0.936 -0.414 L -1.448 -0.414 L -0.684 -2.515 L -0.123 -2.515 Z M -0.149 -1.245 L -0.375 -1.951 Q -0.4 -2.03 -0.41 -2.14 L -0.421 -2.14 Q -0.429 -2.047 -0.458 -1.956 L -0.687 -1.245 Z" stroke-width="0.1"/>
    </g>
    
    <g name="signal-t" {create_primary_icon_style(qgis_render, dark_mode)} >
      <path d="M 0.314 -2.13 L -0.285 -2.13 L -0.285 -0.415 L -0.759 -0.415 L -0.759 -2.13 L -1.356 -2.13 L -1.356 -2.516 L 0.314 -2.516 Z" stroke-width="0.1"/>
    </g>
    
    <g name="shunting-area-lamp" class="animated" {create_secondary_icon_style(qgis_render, dark_mode)} >
      <circle class="aspect-on-off" cx="1.25" cy="0" r="0.75" fill="{IconStyleEnum.gold}" stroke="none" />
      <line x1="2" x2="0.5" y1="-0.75" y2="0.75" />
      <line x1="0.5" x2="2" y1="-0.75" y2="0.75" />
      <line x1="0" x2="1.5" y1="0" y2="0.00" />
    </g>

    <g name="signal-spreader-lens" {create_secondary_icon_style(qgis_render, dark_mode)} >
        <line x1="0.75" x2="2" y1="-2.25" y2="0" />
        <line x1="2" x2="3.25" y1="0" y2="-2.25" />
    </g>

    <g name="signal-white-bar" class="animated" {create_secondary_icon_style(qgis_render, dark_mode)} >
        <line class="aspect-count-down-bar" x1="0" x2="4" y1="0" y2="0" />
    </g>

    <g name="signal-out-of-service" {create_primary_icon_style(qgis_render, dark_mode)} >
        <line x1="-2" x2="2" y1="2" y2="-2" />
        <line x1="-2" x2="2" y1="-2" y2="2" />
    </g>

    <g name="signal-danger-sign" {create_primary_icon_style(qgis_render, dark_mode)} >
        <rect x="-1.125" y="-1.125" width="2.25" height="2.25" fill="{IconStyleEnum.gray}" />
        <line x1="-0.4125" x2="-0.4125" y1="1.125" y2="-1.125" stroke="{IconStyleEnum.black}" />       
        <line x1="0.4125" x2="0.4125" y1="1.125" y2="-1.125" stroke="{IconStyleEnum.black}" />
        <rect x="-1.125" y="-1.125" width="2.25" height="2.25" fill="none"  />
    </g>

    <g name="arrow-sign" {create_primary_icon_style(qgis_render, dark_mode)} > 
        <rect x="0" y="0" width="1.412" height="2.384" fill="{IconStyleEnum.gray}" />
        <line x1="0.755" y1="1.228" x2="0.743" y2="1.958" stroke="{IconStyleEnum.black}" stroke-width="0.1" />
        <path d="M 0.751 0.527 L 1.047 1.279 L 0.455 1.279 L 0.751 0.527 Z" fill="{IconStyleEnum.black}" stroke="{IconStyleEnum.black}" stroke-width="0.1"/>
    </g>
    
    <g name="arrow-sign-double" {create_primary_icon_style(qgis_render, dark_mode)} >
      <rect x="0" y="0" width="1.412" height="2.384" fill="{IconStyleEnum.gray}" />
      <line x1="0.706" y1="1.592" x2="0.228" y2="1.04" stroke-width="0.1" stroke="{IconStyleEnum.black}" />
      <path d="M 1.175 2.113 L 0.454 1.749 L 0.896 1.355 L 1.175 2.113 Z" fill="{IconStyleEnum.black}" stroke="{IconStyleEnum.black}" stroke-width="0.1" />
      <line x1="0.705" y1="0.842" x2="0.228" y2="1.394" stroke-width="0.1" stroke="{IconStyleEnum.black}" />
      <path d="M 1.175 0.321 L 0.454 0.685 L 0.896 1.079 L 1.175 0.321 Z" fill="{IconStyleEnum.black}" stroke="{IconStyleEnum.black}" stroke-width="0.1" />
    </g>

    <g name="signal-direction-sign" {create_secondary_icon_style(qgis_render, dark_mode)} >
      <polygon points="1 -1.823 2 -1.823 1 0 2 1.816 1 1.816 0 0" stroke-width="0.2" fill="{IconStyleEnum.gray}" />
    </g>

    <g name="signal-direction-3-sign" {create_secondary_icon_style(qgis_render, dark_mode)} >
      <polygon points="1 -1.8230 2 -1.8230 1.1680 -0.33300 2 -0.33300 2 0.30800 1.1540 0.30800 2 1.8160 1 1.8160 0 0 " stroke-width="0.2" fill="{IconStyleEnum.gray}" />
    </g> 


    <!-- Sign base -->
    <g name="sign-normal-base" {create_primary_icon_style(qgis_render, dark_mode)} >
        <line x1="0" x2="0" y1="-1.45" y2="1.45" />
        <line x1="10" x2="0" y1="0" y2="0" />
    </g>

    <g name="sign-lowered-base" {create_primary_icon_style(qgis_render, dark_mode)} >
      <line x1="0" x2="0" y1="-1" y2="1" />
      <line x1="4" x2="0" y1="0" y2="0" />
    </g>

    <g name="sign-rectangle" >
        <rect x="0" y="-2" width="4" height="4" fill="{IconStyleEnum.white}"/>
    </g>

    <g name="sign-rectangle-no-fill" {create_primary_icon_style(qgis_render, dark_mode)} >
        <rect x="0" y="-2" width="4" height="4" fill="none" />
    </g>

    <g name="sign-rectangle-45-degrees" {create_primary_icon_style(qgis_render, dark_mode)} >
        <polygon points="0 -2.827 2.826 0 0 2.829 -2.83 0" />
    </g>

    <g name="sign-rectangle-45-degrees-no-fill" {create_primary_icon_style(qgis_render, dark_mode)} >
        <polygon points="0 -2.827 2.826 0 0 2.829 -2.83 0" fill="none" />
    </g>

    <!-- SpeedSigns -->
    <g name="RS-314" {create_primary_icon_style(qgis_render, dark_mode)} >
        <rect x="0" y="-2" width="4" height="4" fill="{IconStyleEnum.white}" />
    </g>

    <g name="RS-313" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path d="M 0 0 L 5.6 2.8 L 5.6 -2.8 Z" fill="{IconStyleEnum.gold}" />
    </g>

    <g name="RS-316" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path d="M 5.6 0 L 0 -2.8 L 0 2.8 Z" fill="{IconStyleEnum.green}" />
    </g>

    <!-- Signs -->
    <g name="sign-bottom-plate" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path d="M 0 2 L 1 2 L 1 -2 L 0 -2 Z" fill="{IconStyleEnum.white}" />
    </g>

    <g name="sign-doghouse" {create_primary_icon_style(qgis_render, dark_mode)} >
      <path d="M2,-2 L0,-2 L0,2 L2,2 L4,0 L2,-2 Z " fill="{IconStyleEnum.white}"/>
    </g>

    <g name="sign-doghouse-no-fill" {create_primary_icon_style(qgis_render, dark_mode)} >
      <path d="M2,-2 L0,-2 L0,2 L2,2 L4,0 L2,-2 Z " fill="none"/>
    </g>

    <g name="RS-375" class="doghouse-o" {create_primary_icon_style(qgis_render, dark_mode)} >
        <circle cx="2" cy="0" r="0.75" fill="none" stroke="{IconStyleEnum.black}"/>
    </g>

    <g name="RS-301" class="doghouse-s" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path d="M 1.193 0.331 C 1.193 0.331 0.885 0.151 0.719 0.158 C 0.547 0.166 0.250 0.331 0.182 0.462 C 0.114 0.602 0.152 0.89 0.265 1.000 C 0.401 1.134 0.890 0.974 1.036 1.104 C 1.162 1.216 1.209 1.494 1.173 1.65 C 1.140 1.791 1.004 1.952 0.870 2.009 C 0.689 2.069 0.440 2.041 0.294 1.969 C 0.114 1.897 -0.078 1.588 -0.078 1.588" fill="none" stroke="{IconStyleEnum.black}"/>
    </g>


    <g name="RS-300" {create_primary_icon_style(qgis_render, dark_mode)} >
        <line x1="2.5875" x2="2.4219" y1="0.675" y2="0.3582" stroke="{IconStyleEnum.red}" />
        <line x1="2.2113" x2="2.124" y1="1.0323" y2="0.864" stroke="{IconStyleEnum.red}" />
        <line x1="1.8486" x2="1.7073" y1="1.4139" y2="1.1448" stroke="{IconStyleEnum.red}" />
        <line x1="1.4787" x2="1.1934" y1="1.7838" y2="1.2366" stroke="{IconStyleEnum.red}" />
        <line x1="0.9243" x2="0.5058" y1="1.8" y2="0.9981" stroke="{IconStyleEnum.red}" />
        <line x1="0.3618" x2="-0.3375" y1="1.8" y2="0.459" stroke="{IconStyleEnum.red}" />
        <line x1="2.9574" x2="2.2905" y1="0.3051" y2="-0.972" stroke="{IconStyleEnum.red}" />
        <line x1="0" x2="-0.3375" y1="0.0288" y2="-0.6183" stroke="{IconStyleEnum.red}" />
        <line x1="0.198" x2="-0.3375" y1="-0.6714" y2="-1.6965" stroke="{IconStyleEnum.red}" />
        <line x1="0.5679" x2="0.171" y1="-1.0404" y2="-1.8" stroke="{IconStyleEnum.red}" />
        <line x1="1.0359" x2="0.7335" y1="-1.2213" y2="-1.8" stroke="{IconStyleEnum.red}" />
        <line x1="1.6218" x2="1.296" y1="-1.1763" y2="-1.8" stroke="{IconStyleEnum.red}" />
    </g>

    <g name="RS-301b" {create_primary_icon_style(qgis_render, dark_mode)} >
        <rect x="0" y="-2" width="2" height="4" fill="{IconStyleEnum.white}" />
        <path d="M 0 2 L 0 0.667 L 0 0.507 L 1.5 2 L 0 2" fill="{IconStyleEnum.red}" stroke="{IconStyleEnum.black}" />
        <path d="M 0 -1.5 L 0 -0.466 L 2 1.5 L 2 0.48 L 0 -1.5" fill="{IconStyleEnum.red}" stroke="{IconStyleEnum.black}" />
        <path d="M 2  -0.5 L 2 -1.985 L 0.515 -1.985 L 2 -0.5" fill="{IconStyleEnum.red}" stroke="{IconStyleEnum.black}" />
        <rect x="0" y="-2" width="2" height="4" fill="none" />
    </g>


<!-- this is example -->
    <g name="RS-513" {create_primary_icon_style(qgis_render, dark_mode)} >
        <rect y="-2" width="2" height="4" fill="{IconStyleEnum.white}" />
        <path d="M 0.75 -2 L 1.25 -2 L 1.25 2 L 0.75 2 L 0.75 -2" fill="{IconStyleEnum.red}" stroke-width="0.1" stroke="{IconStyleEnum.black}"/>
        <rect y="-2" width="2" height="4" fill="none" />
    </g>
    
    <g name="RS-243" >
        <rect y="-2" width="4" height="4" fill="{IconStyleEnum.white}"/>
        <path d="M 1.791 -2 L 2.581 -2 L 2.581 2 L 1.311 2 L 1.311 -2" stroke-width="0.1" fill="{IconStyleEnum.red}" style=""/>
        <rect y="-2" width="2" height="4" fill="none"/>
    </g>


    <g name="RS-244a" {create_primary_icon_style(qgis_render, dark_mode)} >
        <rect x="0" y="-2" width="5" height="4" fill="{IconStyleEnum.black}" />
        <rect x="0.5" y="-1" width="4" height="2" fill="{IconStyleEnum.white}" stroke="{IconStyleEnum.black}" stroke-width="0.5" />
    </g>

    <g name="RS-307a" {create_primary_icon_style(qgis_render, dark_mode)} >
        <polygon points="0,-2.75 2.828,0.078 0,2.906 -2.828,0.078" fill="{IconStyleEnum.blue}" stroke="{IconStyleEnum.black}" />
        <rect x="0.804" y="-1.019" width="0.272" height="1.583" stroke="{IconStyleEnum.white}" fill="{IconStyleEnum.white}" />
        <rect x="-1" y="-1.019" width="0.313" height="1.583" stroke="{IconStyleEnum.white}" fill="{IconStyleEnum.white}" />
        <rect x="-1" y="0.564" width="2.071" height="0.294" stroke="{IconStyleEnum.white}" fill="{IconStyleEnum.white}" />
    </g>

    <g name="RS-311" {create_primary_icon_style(qgis_render, dark_mode)} >
        <polygon points="0,-2.75 2.828,0.078 0,2.906 -2.828,0.078" fill="{IconStyleEnum.blue}" stroke="{IconStyleEnum.white}" />
        <polygon points="0,-1.7325 1.78164,0.04914 0,1.83078 -1.78164,0.04914" fill="{IconStyleEnum.white}" stroke="{IconStyleEnum.blue}"/>
        <polygon points="0,-0.825 0.8484,0.0234 0,0.8718 -0.8484,0.0234" fill="{IconStyleEnum.white}" stroke="{IconStyleEnum.blue}" />
    </g>

    <g name="RS-311-left" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path d="M 0 -3.375 L 4.875 -3.375 L 4.875 -0.5 L 2.875 -0.5 L 0 -3.375" fill="{IconStyleEnum.blue}" />
        <line x1="3.125" x2="3.75" y1="-1.125" y2="-2.875" stroke="{IconStyleEnum.white}" />
        <line x1="3.75" x2="4.5" y1="-2.875" y2="-1.125" stroke="{IconStyleEnum.white}" />
    </g>

    <g name="RS-311-right" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path d="M 0 -3.375 L -4.875 -3.375 L -4.875 -0.5 L -2.875 -0.5 L 0 -3.375" fill="{IconStyleEnum.blue}" />
        <line x1="-3.125" x2="-3.75" y1="-1.125" y2="-2.875" stroke="{IconStyleEnum.white}" />
        <line x1="-3.75" x2="-4.5" y1="-2.875" y2="-1.125" stroke="{IconStyleEnum.white}" />
    </g>

    <g name="RS-308a" {create_primary_icon_style(qgis_render, dark_mode)} >
        <polygon points="0,-2.75 2.828,0.078 0,2.906 -2.828,0.078" />
        <path d="M -0.482 -1.277 L 1.478 -1.277"/>
        <path d="M -0.482 -1.034 L 1.724 -1.034"/>
        <path d="M -1.511 1.348 L 0.311 1.348"/>
        <path d="M -1.708 1.149 L 0.311 1.149"/>
    </g>

    <g name="RS-RS309-RS-310a" {create_primary_icon_style(qgis_render, dark_mode)} >
        <polygon points="0,-2.75 2.828,0.078 0,2.906 -2.828,0.078" fill="{IconStyleEnum.blue}" stroke="{IconStyleEnum.white}" />
        <path d="M 0 -2.68 L 0 2.777" stroke="{IconStyleEnum.white}"/>
        <path d="M -0.233 -2.431 L -0.233 2.601" stroke="{IconStyleEnum.white}"/>
        <path d="M 0.247 -2.431 L 0.247 2.601" stroke="{IconStyleEnum.white}"/>
        <path d="M -0.525 -2.176 L -0.525 2.324" stroke="{IconStyleEnum.white}"/>
        <path d="M 0.505 -2.154 L 0.505 2.346" stroke="{IconStyleEnum.white}"/>
        <polygon points="0, -2.37875 2.44882, 0.06757 0, 2.51519 -2.44882, 0.06757" fill="none" stroke="{IconStyleEnum.black}" />
    </g>

    <g name="RS-249" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path d="M 7.25 1 L 12.25 1 L 12.25 -1 L 7.25 -1 L 7.25 1" fill="{IconStyleEnum.white}" />
        <path d="M 0 1 L 5 1 L 5 -1 L 0 -1 L 0 1" fill="{IconStyleEnum.white}" />
        <path d="M 14.5 1 L 19.5 1 L 19.5 -1 L 14.5 -1 L 14.5 1" fill="{IconStyleEnum.white}" />
        <line x1="9.25" x2="11.25" y1="-1" y2="1" stroke="{IconStyleEnum.black}" />
        <line x1="8.25" x2="10.25" y1="-1" y2="1" stroke="{IconStyleEnum.black}" />
        <line x1="1.5" x2="3.5" y1="-1" y2="1" stroke="{IconStyleEnum.black}" />
        <line x1="17" x2="19" y1="-1" y2="1" stroke="{IconStyleEnum.black}" />
        <line x1="16" x2="18" y1="-1" y2="1" stroke="{IconStyleEnum.black}" />
        <line x1="15" x2="17" y1="-1" y2="1" stroke="{IconStyleEnum.black}" />
        <path d="M 7.25 1 L 12.25 1 L 12.25 -1 L 7.25 -1 L 7.25 1" fill="None" />
        <path d="M 0 1 L 5 1 L 5 -1 L 0 -1 L 0 1" fill="None" />
        <path d="M 14.5 1 L 19.5 1 L 19.5 -1 L 14.5 -1 L 14.5 1" fill="None" />
    </g>

    <g name="RS-251a-II" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path d="M 7.25 1 L 12.25 1 L 12.25 -1 L 7.25 -1 L 7.25 1" fill="{IconStyleEnum.gold}"/>
        <path d="M 0 1 L 5 1 L 5 -1 L 0 -1 L 0 1" fill="{IconStyleEnum.gold}"/>
        <path d="M 14.5 1 L 19.5 1 L 19.5 -1 L 14.5 -1 L 14.5 1" fill="{IconStyleEnum.gold}"/>
        <line x1="9.25" x2="11.25" y1="-1" y2="1" stroke="{IconStyleEnum.black}" />
        <line x1="8.25" x2="10.25" y1="-1" y2="1" stroke="{IconStyleEnum.black}" />
        <line x1="1.5" x2="3.5" y1="-1" y2="1" stroke="{IconStyleEnum.black}" />
        <line x1="17" x2="19" y1="-1" y2="1" stroke="{IconStyleEnum.black}" />
        <line x1="16" x2="18" y1="-1" y2="1" stroke="{IconStyleEnum.black}" />
        <line x1="15" x2="17" y1="-1" y2="1" stroke="{IconStyleEnum.black}" />
        <path d="M 7.25 1 L 12.25 1 L 12.25 -1 L 7.25 -1 L 7.25 1" fill="None"/>
        <path d="M 0 1 L 5 1 L 5 -1 L 0 -1 L 0 1" fill="None"/>
        <path d="M 14.5 1 L 19.5 1 L 19.5 -1 L 14.5 -1 L 14.5 1" fill="None"/>
    </g>

    <g name="RS-249a" {create_primary_icon_style(qgis_render, dark_mode)} >
        <path d="M 7.25 1 L 12.25 1 L 12.25 -1 L 7.25 -1 L 7.25 1" fill="{IconStyleEnum.white}" />
        <path d="M 0 1 L 5 1 L 5 -1 L 0 -1 L 0 1" fill="{IconStyleEnum.white}" />
        <path d="M 14.5 1 L 19.5 1 L 19.5 -1 L 14.5 -1 L 14.5 1" fill="{IconStyleEnum.white}" />
        <path d="M -2.5 -1.25 L 0 0 L -2.5 1.25 L -2.5 -1.25" fill="{IconStyleEnum.white}" />
        <line x1="10.75" x2="9.75" y1="-0" y2="1" />
        <line x1="9.75" x2="10.75" y1="-1" y2="0" />
        <line x1="16.5" x2="15.5" y1="-0" y2="1" />
        <line x1="15.5" x2="16.5" y1="-1" y2="0" />
        <line x1="18.5" x2="17.5" y1="-0" y2="1" />
        <line x1="9.75" x2="8.75" y1="-0" y2="1" />
        <line x1="8.75" x2="9.75" y1="-1" y2="0" />
        <line x1="2.25" x2="1.25" y1="-0" y2="1" />
        <line x1="1.25" x2="2.25" y1="-1" y2="0" />
        <line x1="17.5" x2="16.5" y1="-0" y2="1" />
        <line x1="16.5" x2="17.5" y1="-1" y2="0" />
        <line x1="17.5" x2="18.5" y1="-1" y2="0" />
    </g>

    <g name="RS-318" {create_primary_icon_style(qgis_render, dark_mode)} >
        <circle cx="0" cy="0" r="2" fill="{IconStyleEnum.white}" />
        <circle cx="0" cy="0" r="1.5" fill="{IconStyleEnum.white}" stroke="{IconStyleEnum.black}" stoke-width="0.2" />

    </g>

    <g name="RS-331" {create_primary_icon_style(qgis_render, dark_mode)} >
        <rect x="2" y="-2" width="3" height="4" fill="{IconStyleEnum.white}"/>
        <rect x="6" y="-2" width="5" height="4" fill="{IconStyleEnum.white}"/>
        <line x1="0" x2="0" y1="-1" y2="1" />
        <line x1="0" x2="2" y1="-0" y2="-0" />
        <line x1="5" x2="6" y1="-0" y2="-0" />
        <line x1="7" x2="10" y1="-0" y2="-0" stroke="{IconStyleEnum.black}" />
        <line x1="8" x2="8" y1="1" y2="-1" stroke="{IconStyleEnum.black}" />
    </g>    

    <g name="RS-305" {create_primary_icon_style(qgis_render, dark_mode)} >
        <rect x="2.25" y="-1" width="6" height="2" fill="{IconStyleEnum.white}" />
        <line x1="2.25" y1="0" x2="0" y2="0"/>
        <line x1="0" y1="-1.25" x2="0" y2="1.25"/>
        <path d="M 3.547 -0.538 C 3.547 -0.538 3.152 -0.326 3.083 -0.213 C 3.041 -0.144 3.045 -0.075 3.054 0 C 3.065 0.091 3.085 0.215 3.172 0.29 C 3.313 0.412 3.702 0.495 3.971 0.487 C 4.251 0.478 4.531 0.34 4.819 0.221 C 5.141 0.088 5.536 -0.176 5.805 -0.292 C 5.982 -0.368 6.094 -0.423 6.259 -0.45 C 6.445 -0.48 6.687 -0.467 6.871 -0.44 C 7.027 -0.417 7.199 -0.403 7.295 -0.321 C 7.381 -0.248 7.463 -0.113 7.443 0 C 7.413 0.164 6.91 0.527 6.91 0.527" fill="none" stroke="{IconStyleEnum.black}" />
    </g>

    <g name="RS-304a" {create_primary_icon_style(qgis_render, dark_mode)} >
        <polygon points="0.011 -2.028 2.038 -0.002 0.011 2.024 -2.016 -0.002" fill="{IconStyleEnum.blue}" stroke="{IconStyleEnum.white}" />        
    </g>


    <!-- TODO: refactor below so we not transposing like a... -->
    <g name="RS-304c" {create_primary_icon_style(qgis_render, dark_mode)} >
        <polygon points="0.011 -1.958 2.038 0.068 0.011 2.094 -2.016 0.068" fill="{IconStyleEnum.blue}" stroke="none" />
        <path d="M 0.013 -1.958 L 2.038 0.069 L -2.013 0.069 L 0.013 -1.958 Z" fill="{IconStyleEnum.white}" stroke="none" />

    </g>


    <!-- TODO: fix CAB text, is so dam ugly-->
    <g name="RS-336" {create_primary_icon_style(qgis_render, dark_mode)} >
        <rect x="0" y="-2.5" width="3" height="5" fill="{IconStyleEnum.white}" />
        <path d="M 1.301 -1.09 L 1.199 -0.816 C 1.02 -0.859 0.887 -0.929 0.8 -1.025 C 0.713 -1.123 0.669 -1.247 0.669 -1.396 C 0.669 -1.582 0.744 -1.734 0.893 -1.854 C 1.042 -1.973 1.245 -2.032 1.503 -2.032 C 1.776 -2.032 1.988 -1.972 2.139 -1.852 C 2.29 -1.733 2.366 -1.575 2.366 -1.379 C 2.366 -1.208 2.307 -1.07 2.188 -0.963 C 2.118 -0.9 2.017 -0.852 1.886 -0.821 L 1.808 -1.1 C 1.893 -1.116 1.96 -1.15 2.009 -1.203 C 2.058 -1.255 2.083 -1.319 2.083 -1.394 C 2.083 -1.498 2.039 -1.581 1.952 -1.646 C 1.865 -1.71 1.723 -1.742 1.528 -1.742 C 1.321 -1.742 1.173 -1.711 1.085 -1.648 C 0.997 -1.584 0.952 -1.501 0.952 -1.399 C 0.952 -1.325 0.98 -1.26 1.037 -1.206 C 1.093 -1.152 1.181 -1.114 1.301 -1.09 Z M 0.697 0.684 L 0.697 0.377 L 1.07 0.255 L 1.07 -0.302 L 0.697 -0.418 L 0.697 -0.717 L 2.338 -0.173 L 2.338 0.124 L 0.697 0.684 Z M 1.347 0.165 L 1.955 -0.027 L 1.347 -0.215 L 1.347 0.165 Z M 2.338 0.834 L 2.338 1.392 C 2.338 1.503 2.332 1.585 2.322 1.639 C 2.311 1.693 2.289 1.742 2.255 1.785 C 2.22 1.828 2.174 1.863 2.117 1.893 C 2.06 1.92 1.996 1.935 1.925 1.935 C 1.848 1.935 1.778 1.916 1.714 1.882 C 1.649 1.846 1.601 1.799 1.569 1.738 C 1.54 1.824 1.49 1.89 1.42 1.935 C 1.35 1.98 1.268 2.003 1.173 2.003 C 1.098 2.003 1.026 1.988 0.956 1.958 C 0.885 1.93 0.828 1.889 0.786 1.838 C 0.744 1.787 0.718 1.724 0.709 1.65 C 0.703 1.602 0.699 1.489 0.697 1.309 L 0.697 0.834 L 2.338 0.834 Z M 2.065 1.115 L 1.685 1.115 L 1.685 1.3 C 1.685 1.41 1.687 1.479 1.691 1.505 C 1.698 1.554 1.718 1.592 1.75 1.619 C 1.782 1.646 1.825 1.661 1.878 1.661 C 1.929 1.661 1.97 1.649 2.002 1.625 C 2.034 1.601 2.053 1.565 2.06 1.518 C 2.063 1.491 2.065 1.409 2.065 1.278 L 2.065 1.115 Z M 1.412 1.115 L 0.974 1.115 L 0.974 1.377 C 0.974 1.479 0.977 1.542 0.984 1.57 C 0.993 1.612 1.015 1.646 1.05 1.673 C 1.084 1.699 1.131 1.712 1.189 1.712 C 1.238 1.712 1.28 1.702 1.314 1.682 C 1.349 1.661 1.373 1.632 1.389 1.594 C 1.405 1.556 1.412 1.472 1.412 1.344 L 1.412 1.115 Z" fill="{IconStyleEnum.black}" stroke-width="0.1"/>
    </g>

    <g name="RS-337" {create_primary_icon_style(qgis_render, dark_mode)} >
        <line x1="0.019" y1="-2.503" x2="3" y2="2.5" transform="matrix(1, 0, 0, 1, 1.7763568394002505e-15, -8.881784197001252e-16)"/>        
    </g>

    <g name="RS-226a-under-sign" {create_primary_icon_style(qgis_render, dark_mode)} >
        <rect x="0" y="-1" width="1" height="2" fill="{IconStyleEnum.white}"/>
    </g>

    <g name="RS-253" {create_primary_icon_style(qgis_render, dark_mode)} >
      <rect width="4" height="4" fill="{IconStyleEnum.blue}" />
      <polyline points="4 0.554 0.232 1.989" stroke="{IconStyleEnum.white}" />
      <polyline points="3.979 3.685 0.243 2.028" stroke="{IconStyleEnum.white}" />
      <line x1="0.241" y1="1.756" x2="0.241" y2="2.256" fill="{IconStyleEnum.white}" stroke="{IconStyleEnum.white}" />
      <rect width="4" height="4" x="-0.021" fill="none" />  
    </g>

    <g name="RS-333" {create_primary_icon_style(qgis_render, dark_mode)} >
        <polygon points="0,-2.75 2.828,0.078 0,2.906 -2.828,0.078" fill="{IconStyleEnum.white}" />
        <line x1="-1.499" y1="1.398" x2="1.346" y2="-1.393" stroke="{IconStyleEnum.black}" />
        <line x1="0" y1="1.398" x2="0" y2="-1" stroke="{IconStyleEnum.black}" />
        <line x1="0.491" y1="1.398" x2="-0.509" y2="1.398" stroke="{IconStyleEnum.black}" />
        <circle cx="-0.013" cy="-1.143" r="0.45" stroke="{IconStyleEnum.black}" fill="{IconStyleEnum.black}" />
    </g>

    <g name="RS-306a" fill="{IconStyleEnum.white}" stroke="{IconStyleEnum.white}" stroke-width="0.2">
        <polygon points="0,-2.75 2.828,0.078 0,2.906 -2.828,0.078" fill="{IconStyleEnum.blue}" stroke="{IconStyleEnum.black}" />
        <rect x="0.804" y="-1.019" width="0.272" height="0.562" />
        <rect x="-0.995" y="-1.019" width="0.272" height="0.562" />
        <rect x="-0.995" y="0.564" width="2.071" height="0.294" />
    </g>

    <g name="RS-308a" fill="{IconStyleEnum.white}" stroke="{IconStyleEnum.white}" stroke-width="0.3">
        <polygon points="0 -2.827 2.826 0 0 2.829 -2.83 0" fill="{IconStyleEnum.blue}" stroke-width="0.2"/>
        <line x1="1.338" y1="1.48" x2="1.338" y2="-0.56" />
        <line x1="1.085" y1="1.742" x2="1.085" y2="-0.56" />
        <line x1="-0.895" y1="0.369" x2="-0.895" y2="-1.933" />
        <line x1="-1.176" y1="0.369" x2="-1.176" y2="-1.648"/>
    </g>

    <g name="RS-328a" fill="{IconStyleEnum.white}" stroke="{IconStyleEnum.white}" stroke-width="0.3">
        <path d="M0-2.827 2.826 0 0 2.829-2.83 0z" style="stroke: rgb(0, 0, 0); stroke-width: 0.5px; fill: rgb(245, 199, 13);"/>
        <path style="stroke-width: 0px; fill: rgb(0, 114, 183);" d="M -2.455 -0.016 L 0.039 -0.003 L 0.001 -2.51 L -2.455 -0.016 Z"/>
        <path style="stroke-width: 0px; fill: rgb(0, 114, 183);" d="M 0.008 -0.022 L 2.501 -0.01 L 0.007 2.465 L 0.008 -0.022 Z"/>
        <circle style="fill:#d8d8d8;stroke-width:1px;stroke:none" cx="-.60" cy="-.65" r=".3" stroke="none"/>
        <circle style="fill:#d8d8d8;stroke-width:1px;stroke:none" cx=".65" cy=".60" r=".3" stroke="none"/>
    </g>


    <g name="RS-328" fill="{IconStyleEnum.white}" stroke="{IconStyleEnum.black}" stroke-width="0.5">
        <polygon points="0 -2.827 2.826 0 0 2.829 -2.83 0" stroke-width="0.2" style="fill: rgb(245, 199, 13);"/>
        <path d="M -0.395 0.564 L -0.662 0.564 L -0.768 0.288 L -1.255 0.288 L -1.355 0.564 L -1.616 0.564 L -1.142 -0.653 L -0.882 -0.653 Z M -0.847 0.083 L -1.015 -0.369 L -1.179 0.083 Z M -0.117 0.564 L -0.117 -0.447 L -0.478 -0.447 L -0.478 -0.653 L 0.489 -0.653 L 0.489 -0.447 L 0.129 -0.447 L 0.129 0.564 Z M 0.648 -0.653 L 1.135 -0.653 Q 1.279 -0.653 1.35 -0.641 Q 1.421 -0.629 1.477 -0.591 Q 1.533 -0.552 1.57 -0.489 Q 1.608 -0.425 1.608 -0.347 Q 1.608 -0.261 1.562 -0.19 Q 1.516 -0.118 1.437 -0.083 Q 1.548 -0.05 1.608 0.028 Q 1.668 0.106 1.668 0.211 Q 1.668 0.294 1.629 0.373 Q 1.59 0.451 1.523 0.498 Q 1.457 0.545 1.359 0.556 Q 1.297 0.562 1.062 0.564 L 0.648 0.564 Z M 0.894 -0.45 L 0.894 -0.169 L 1.055 -0.169 Q 1.199 -0.169 1.233 -0.173 Q 1.296 -0.181 1.333 -0.217 Q 1.369 -0.253 1.369 -0.312 Q 1.369 -0.368 1.338 -0.403 Q 1.306 -0.439 1.245 -0.446 Q 1.208 -0.45 1.035 -0.45 Z M 0.894 0.034 L 0.894 0.359 L 1.121 0.359 Q 1.254 0.359 1.29 0.352 Q 1.345 0.342 1.379 0.303 Q 1.414 0.264 1.414 0.2 Q 1.414 0.145 1.387 0.107 Q 1.36 0.068 1.31 0.051 Q 1.26 0.034 1.092 0.034 Z" style="fill: rgb(0, 0, 0); stroke: none; text-wrap-mode: nowrap;"/>
    </g>
    
    <g name="RS-328b" fill="{IconStyleEnum.white}" stroke="{IconStyleEnum.black}" stroke-width="0.3">
        <polygon points="0 -2.827 2.826 0 0 2.829 -2.83 0" stroke-width="0.3" style="fill: rgb(245, 199, 13);"/>
        <path d="M -1.131 0.127 L -1.006 0.158 C -1.033 0.261 -1.08 0.339 -1.148 0.393 C -1.217 0.447 -1.3 0.474 -1.398 0.474 C -1.5 0.474 -1.583 0.454 -1.647 0.412 C -1.711 0.371 -1.759 0.31 -1.793 0.232 C -1.826 0.154 -1.842 0.069 -1.842 -0.022 C -1.842 -0.12 -1.824 -0.207 -1.786 -0.28 C -1.749 -0.353 -1.695 -0.408 -1.625 -0.446 C -1.557 -0.484 -1.48 -0.503 -1.396 -0.503 C -1.301 -0.503 -1.222 -0.48 -1.157 -0.431 C -1.094 -0.383 -1.049 -0.315 -1.022 -0.228 L -1.146 -0.199 C -1.168 -0.268 -1.2 -0.318 -1.242 -0.349 C -1.284 -0.38 -1.336 -0.396 -1.398 -0.396 C -1.471 -0.396 -1.532 -0.378 -1.581 -0.344 C -1.63 -0.31 -1.664 -0.263 -1.684 -0.204 C -1.704 -0.145 -1.713 -0.085 -1.713 -0.023 C -1.713 0.058 -1.702 0.128 -1.678 0.188 C -1.655 0.249 -1.618 0.294 -1.569 0.323 C -1.52 0.352 -1.466 0.367 -1.408 0.367 C -1.338 0.367 -1.279 0.347 -1.23 0.307 C -1.182 0.266 -1.149 0.206 -1.131 0.127 Z M -0.89 -0.002 C -0.89 -0.159 -0.849 -0.282 -0.764 -0.371 C -0.68 -0.46 -0.571 -0.504 -0.438 -0.504 C -0.351 -0.504 -0.272 -0.483 -0.202 -0.442 C -0.132 -0.4 -0.078 -0.342 -0.041 -0.267 C -0.005 -0.193 0.013 -0.108 0.013 -0.013 C 0.013 0.083 -0.006 0.168 -0.044 0.244 C -0.083 0.32 -0.138 0.377 -0.209 0.416 C -0.28 0.455 -0.357 0.474 -0.439 0.474 C -0.528 0.474 -0.608 0.453 -0.677 0.41 C -0.748 0.367 -0.8 0.308 -0.837 0.234 C -0.873 0.159 -0.89 0.08 -0.89 -0.002 Z M -0.762 -0.001 C -0.762 0.113 -0.732 0.203 -0.67 0.269 C -0.608 0.335 -0.532 0.367 -0.439 0.367 C -0.345 0.367 -0.268 0.334 -0.207 0.268 C -0.146 0.202 -0.115 0.108 -0.115 -0.014 C -0.115 -0.09 -0.129 -0.158 -0.154 -0.215 C -0.181 -0.273 -0.219 -0.318 -0.269 -0.349 C -0.319 -0.38 -0.375 -0.396 -0.437 -0.396 C -0.526 -0.396 -0.602 -0.366 -0.666 -0.305 C -0.73 -0.244 -0.762 -0.142 -0.762 -0.001 Z M 0.175 0.458 L 0.175 -0.487 L 0.5 -0.487 C 0.574 -0.487 0.63 -0.483 0.669 -0.473 C 0.723 -0.461 0.769 -0.438 0.807 -0.406 C 0.857 -0.364 0.895 -0.31 0.919 -0.244 C 0.944 -0.178 0.956 -0.104 0.956 -0.02 C 0.956 0.052 0.947 0.116 0.931 0.171 C 0.914 0.227 0.893 0.272 0.866 0.308 C 0.84 0.345 0.812 0.374 0.781 0.395 C 0.749 0.415 0.712 0.431 0.668 0.442 C 0.623 0.453 0.572 0.458 0.516 0.458 L 0.175 0.458 Z M 0.3 0.346 L 0.502 0.346 C 0.563 0.346 0.613 0.341 0.649 0.33 C 0.684 0.318 0.712 0.301 0.733 0.28 C 0.762 0.25 0.785 0.211 0.803 0.161 C 0.819 0.11 0.828 0.05 0.828 -0.022 C 0.828 -0.12 0.811 -0.196 0.779 -0.25 C 0.746 -0.303 0.706 -0.338 0.66 -0.356 C 0.627 -0.369 0.572 -0.376 0.498 -0.376 L 0.3 -0.376 L 0.3 0.346 Z M 1.131 0.458 L 1.131 -0.487 L 1.815 -0.487 L 1.815 -0.376 L 1.256 -0.376 L 1.256 -0.086 L 1.779 -0.086 L 1.779 0.025 L 1.256 0.025 L 1.256 0.346 L 1.837 0.346 L 1.837 0.458 L 1.131 0.458 Z" style="fill: rgb(0, 0, 0); stroke: none; text-wrap-mode: nowrap;" transform="matrix(1, 0, 0, 1, 8.881784197001252e-16, 0)"/>
    </g>

    <g name="RS-329" fill="{IconStyleEnum.white}" stroke="{IconStyleEnum.white}" stroke-width="0.3">
        <polygon points="0 -2.827 2.826 0 0 2.829 -2.83 0" stroke-width="0.3" stroke="{IconStyleEnum.black}" style="fill: rgb(245, 199, 13);"/>
        <path d="M -0.395 0.564 L -0.662 0.564 L -0.768 0.288 L -1.255 0.288 L -1.355 0.564 L -1.616 0.564 L -1.142 -0.653 L -0.882 -0.653 Z M -0.847 0.083 L -1.015 -0.369 L -1.179 0.083 Z M -0.117 0.564 L -0.117 -0.447 L -0.478 -0.447 L -0.478 -0.653 L 0.489 -0.653 L 0.489 -0.447 L 0.129 -0.447 L 0.129 0.564 Z M 0.648 -0.653 L 1.135 -0.653 Q 1.279 -0.653 1.35 -0.641 Q 1.421 -0.629 1.477 -0.591 Q 1.533 -0.552 1.57 -0.489 Q 1.608 -0.425 1.608 -0.347 Q 1.608 -0.261 1.562 -0.19 Q 1.516 -0.118 1.437 -0.083 Q 1.548 -0.05 1.608 0.028 Q 1.668 0.106 1.668 0.211 Q 1.668 0.294 1.629 0.373 Q 1.59 0.451 1.523 0.498 Q 1.457 0.545 1.359 0.556 Q 1.297 0.562 1.062 0.564 L 0.648 0.564 Z M 0.894 -0.45 L 0.894 -0.169 L 1.055 -0.169 Q 1.199 -0.169 1.233 -0.173 Q 1.296 -0.181 1.333 -0.217 Q 1.369 -0.253 1.369 -0.312 Q 1.369 -0.368 1.338 -0.403 Q 1.306 -0.439 1.245 -0.446 Q 1.208 -0.45 1.035 -0.45 Z M 0.894 0.034 L 0.894 0.359 L 1.121 0.359 Q 1.254 0.359 1.29 0.352 Q 1.345 0.342 1.379 0.303 Q 1.414 0.264 1.414 0.2 Q 1.414 0.145 1.387 0.107 Q 1.36 0.068 1.31 0.051 Q 1.26 0.034 1.092 0.034 Z" style="fill: rgb(0, 0, 0); stroke: none; text-wrap-mode: nowrap;"/>
        <polyline style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); stroke-width: 0.75px;" points="1.463 -1.487 -1.398 1.455"/>
    </g>
    
    
    <g name="RS-312" {create_primary_icon_style(qgis_render, dark_mode)}> >
        <polygon points="0.013 -4.546 3.178 -0.013 0.013 4.523 -3.156 -0.013" stroke-width="0.3" style="fill: rgb(255, 255, 255);"/>
        <path d="M -1.094 1.922 L -1.094 -1.657 L 1.321 -1.657 L 1.321 -1.235 L -0.62 -1.235 L -0.62 -0.126 L 1.059 -0.126 L 1.059 0.296 L -0.62 0.296 L -0.62 1.922 Z" stroke="black" fill="black"/>
        <path style="stroke-width: 0px;" d="M 0.006 -4.557 L -0.917 -3.222 L 0.934 -3.234 L 0.006 -4.557 Z" fill="black"/>
        <path style="stroke-width: 0px;" d="M -0.892 3.232 L 0.004 4.546 L 0.922 3.236 L -0.892 3.232 Z" fill="black"/>    
    </g>
        

    <!-- AxleCounterDetection -->

    <g name="axleCounter-base" {create_primary_icon_style(qgis_render, dark_mode)}>  
      <rect x="-2" y="-4" width="4" height="4" style="fill: rgb(255, 255, 255); stroke: rgb(0, 0, 0); stroke-width: 0.25px;"/>
      <polygon style="stroke-linejoin: round; stroke-width: 0;" points="-2 -4 0 0 2 -4"/>
    </g>

    <!-- ATBVVBeacon -->
    <g name="atbVv-Beacon" {create_primary_icon_style(qgis_render, dark_mode)}>
        <rect x="-2" y="-4" width="4" height="4" fill="{IconStyleEnum.white}" stroke="{IconStyleEnum.black}" style="stroke-width: 0.25px;"/>
        <polyline points="-2 -4 2 0" stroke="{IconStyleEnum.black}" style="stroke-width: 0.25px;" />
        <polyline points="-2 0 2 -4" stroke="{IconStyleEnum.black}" style="stroke-width: 0.25px;" />
    </g>

    <!-- InsulatedJoint -->

    <g name="insulatedJoint" {create_primary_icon_style(qgis_render, dark_mode)}>
        <line y1="1.5" y2="-1.5" />
    </g>

    <g name="insulatedJoint-left" {create_primary_icon_style(qgis_render, dark_mode)}>
      <line x1="-.75" y1="-1.5" x2=".75" y2="-1.5" style="stroke-width: 0.25px;" />
    </g>

    <g name="insulatedJoint-right" {create_primary_icon_style(qgis_render, dark_mode)}>
      <line x1="-.75" y1="1.5" x2=".75" y2="1.5" style="stroke-width: 0.25px;" />
    </g>

    <!-- LevelCrossing -->

    <g name="levelCrossing" {create_primary_icon_style(qgis_render, dark_mode)}>
      <path d="M 3.87 -4.122 L 3.87 4 L 11.992 -0.062 L 3.87 -4.122 Z M 4.385 -3.289 L 10.841 -0.062 L 4.385 3.167 L 4.385 -3.289 Z" fill="red" style="stroke: rgb(186, 218, 85); stroke-width: 0px;" />
      <path d="M 6.529 1.6 L 6.202 1.6 L 6.202 -1.589 L 6.529 -1.589 L 6.529 1.6 Z M 5.547 1.6 L 5.219 1.6 L 5.219 -1.589 L 5.547 -1.589 L 5.547 1.6 Z" />
      <path d="M 6.857 -0.663 L 7.514 -1.023 L 6.857 -1.383 L 4.78 -1.383 L 4.78 -0.663 L 6.857 -0.663 Z M 6.859 0.365 L 7.514 0.005 L 6.859 -0.354 L 4.781 -0.354 L 4.781 0.365 L 6.859 0.365 Z M 6.859 1.395 L 7.514 1.034 L 6.859 0.674 L 4.781 0.674 L 4.781 1.395 L 6.859 1.395 Z" style="stroke: rgb(186, 218, 85); stroke-width: 0px;" />
      <rect y="-4" width="5" height="8" style="stroke: rgb(0, 0, 0); fill: rgb(255, 255, 255);" x="-2.5" />
    </g>
    
    
    """
    tree = ET.ElementTree(ET.fromstring(f"<root>{svg_data}</root>"))

    root = tree.getroot()
    svg_dict = {}

    for g in root.findall("g"):
        g_id = g.get("name")
        svg_dict[g_id] = ET.tostring(g, encoding="unicode", method="xml").strip()

    return svg_dict


SVG_SVG_GROUP_DICT = get_svg_groups()
SVG_SVG_GROUP_DICT_DARK = get_svg_groups(dark_mode=True)

QGIS_SVG_GROUP_DICT = get_svg_groups(qgis_render=True)
QGIS_SVG_GROUP_DICT_DARK = get_svg_groups(qgis_render=True, dark_mode=True)
