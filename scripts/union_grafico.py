from great_tables import GT, md
import polars as pl
from selenium import webdriver
from PIL import Image, ImageOps
from datetime import datetime, timedelta, date
import os

# Importar los datos de los otros scripts
from euroligue import df_partidos_euroleague
from eurocup import df_partidos_eurocup
from fiba_championsleague import data_championsleague
from fiba_europecup import data_europecup

# directorios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "png")
OUTPUT_FILE = "desarrollo_europeo_py.png"

# Crear directorio png si no existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Calcular fechas
hoy = datetime.today()
lunes = hoy - timedelta(days=hoy.weekday())
viernes = lunes + timedelta(days=4)
fecha_min = lunes.strftime("%d/%m")
fecha_max = viernes.strftime("%d/%m")
semana = date.today().isocalendar().week

# Caption
twitter = "<span style='color:#000000;font-family: \"Font Awesome 6 Brands\"'>&#xE61A;</span>"
tweetelcheff = "<span style='font-weight:bold;'>*@elcheff*</span>"
insta = "<span style='color:#E1306C;font-family: \"Font Awesome 6 Brands\"'>&#xE055;</span>"
instaelcheff = "<span style='font-weight:bold;'>*@sport_iv0*</span>"
github = "<span style='color:#000000;font-family: \"Font Awesome 6 Brands\"'>&#xF092;</span>"
githubelcheff = "<span style='font-weight:bold;'>*IvoVillanueva*</span>"
caption = f"**Datos**: *@EuroLeague @EuroCup @FIBAEuropeCup @BasketballCL* • **Gráfico**: *Ivo Villanueva* • {twitter} {tweetelcheff} • {insta} {instaelcheff} • {github} {githubelcheff}"


# Funciones
def add_photo_frame(
    color: str, logo: str, container_w: str = "100%", container_h: str = "100%"
) -> pl.Expr:
    return pl.format(
        "<div style='display:flex;align-items:center;justify-content:center;width:{};height:{};'>"
        "<img style='width:86px;height:86px;border-radius:20%;background-color:{};border:2px solid black;'"
        " src='{}' alt=''/></div>",
        pl.lit(container_w),
        pl.lit(container_h),
        pl.col(color),
        pl.col(logo),
    )


def label_html(jugador: str, equipo: str) -> pl.Expr:
    return pl.format(
        "<div style='line-height:1.2;margin-bottom:-4px;text-align:left;'>"
        "<span style='font-size:34px;font-weight:700;color:#000000;'>{}</span><br>"
        "<span style='font-size:26px;font-weight:400;color:#737373;'>{}</span>"
        "</div>",
        pl.col(jugador),
        pl.col(equipo),
    )


def theme_savant(table):
    return table.tab_options(
        table_font_names="Oswald",
        table_font_size="38px",
        column_labels_font_size="28px",
        column_labels_font_weight="bold",
        column_labels_border_top_style="solid",
        column_labels_border_top_color="black",
        column_labels_border_top_width="3px",
        column_labels_border_bottom_color="white",
        table_body_hlines_color="transparent",
        table_border_top_style="none",
        table_border_bottom_style="none",
        table_body_border_bottom_style="none",
        table_body_border_bottom_color="white",
        heading_align="center",
        heading_border_bottom_style="none",
        row_group_border_top_style="none",
        source_notes_font_size="18px",
    )


# Preparar datos
tbl_df = (
    pl.concat([df_partidos_euroleague, df_partidos_eurocup,
               data_championsleague, data_europecup])
    .sort("val", descending=True)
    .head(15)
    .with_columns(
        combo=label_html("player", "equipo"),
        combo_img=add_photo_frame("color", "logo"),
    )
    .select(
        "combo_img",
        "combo",
        "jug",
        "min",
        "pts",
        "reb",
        "ast",
        "bp",
        "br",
        "tap",
        "fa",
        "mm",
        "val",
    )
)

# Crear tabla
table = theme_savant(
    GT(tbl_df)
    .tab_style(
        style=md("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&display=swap');
</style>
"""),
        locations="table"
    )
    .cols_label(
        combo_img="",
        combo="",
        jug="JUG",
        min="MIN",
        pts="PTS",
        reb="REB",
        ast="AST",
        br="BR",
        bp="BP",
        tap="TAP",
        fa="FA",
        mm="+/-",
        val="VAL",
    )
    .cols_width(
        combo_img="120px",
        combo="400px",
        min="90px",
        pts="90px",
        reb="90px",
        ast="90px",
        br="90px",
        bp="90px",
        tap="90px",
        fa="90px",
        mm="90px",
        val="90px",
    )
    .fmt_number(columns=["min", "val"], decimals=0)
    .opt_row_striping(row_striping=True)
    .tab_header(
        title=md(
            f"<div style='display: flex; align-items:center; gap:12px;'>"
            "<img src='https://supermanager.acb.com/assets/images/logo.svg' style='width:144px; height:144px;'/>"
            "<div style='display:flex; flex-direction: column; justify-content: center;'>"
            "<div style='font-weight:600; font-size:68px; line-height:1.2; text-align:left;'>Desarrollo Europeo</div>"
            "<div style='font-weight:400; font-size:35px; color:#8C8C8C; line-height:1.2; text-align:left;'>"
            f"Medias Desde el {fecha_min} al {fecha_max}"
            "</div></div></div>"
        )
    )
    .tab_source_note(md(caption))
)

table.save(f"{OUTPUT_DIR}/{OUTPUT_FILE}")

img = Image.open(f"{OUTPUT_DIR}/{OUTPUT_FILE}")
img_out = ImageOps.expand(img, border=100, fill="white")
img_out.save(f"{OUTPUT_DIR}/desarrollo_europeo_margen_{semana}_.png")
