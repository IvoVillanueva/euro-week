import polars as pl
import pandas as pd
from datetime import datetime, timedelta, date

semana = date.today().isocalendar().week

clubs = pl.read_csv(
    "https://raw.githubusercontent.com/IvoVillanueva/acb2026/refs/heads/main/logos_calendario/clubs2026.csv"
).with_columns(
    [
        pl.when(pl.col("equipo") == "Surne Bilbao Basket")
        .then(pl.lit("#9b51e0"))
        .otherwise(pl.col("color"))
        .alias("color")
    ]
)

data_europecup = (
    pl.read_csv(
        "https://raw.githubusercontent.com/IvoVillanueva/BOXSCORES-EUROLEAGE-2025_26/refs/heads/main/data/boxscores_fiba_europecup_2025-26.csv"
    )
    .with_columns(
        (
            pl.col("TP").str.split(":").list.get(0).cast(pl.Int64)
            + pl.when(pl.col("TP").str.split(":").list.get(1).cast(pl.Int64) >= 30)
            .then(1)
            .otherwise(0)
        ).alias("minutes")
    )
    .filter(pl.col("week") == semana)
    .select(
        [
            "player",
            "equipo",
            "minutes",
            pl.col("PTS").alias("pts"),
            pl.col("REB").alias("reb"),
            pl.col("AS").alias("ast"),
            pl.col("ST").alias("br"),
            pl.col("TO").alias("bp"),
            pl.col("BS").alias("tap"),
            pl.col("PF").alias("fa"),
            pl.col("EFF").alias("val"),
            pl.col("PM").alias("mm"),
        ]
    )
    .join(clubs, on="equipo")
)
