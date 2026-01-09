import polars as pl
import pandas as pd
from datetime import datetime, timedelta, date

semana = date.today().isocalendar().week

clubs = pl.read_csv(
    "https://raw.githubusercontent.com/IvoVillanueva/acb2026/refs/heads/main/logos_calendario/clubs2026.csv"
)

data_championsleague = (
    pl.read_csv(
        "https://raw.githubusercontent.com/IvoVillanueva/BOXSCORES-EUROLEAGE-2025_26/refs/heads/main/data/boxscores_fiba_championsleague_2025-26.csv"
    )
    .with_columns(
        (
            pl.col("TP").str.split(":").list.get(0).cast(pl.Int64)
            + pl.when(pl.col("TP").str.split(":").list.get(1).cast(pl.Int64) >= 30)
            .then(1)
            .otherwise(0)
        ).alias("minutes")
    )
    .filter(
        (
            pl.col("equipo").is_in(
                [
                    "Dreamland Gran Canaria",
                    "Joventut Badalona",
                    "La Laguna Tenerife",
                    "Unicaja",
                ]
            )
        )
        & (pl.col("week") == semana)
    )
    .select(
        [
            "player",
            "equipo",
            pl.col("minutes").alias("min"),
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
    .group_by(["player", "equipo"])
    .agg(
        [   pl.col("player").n_unique().alias("jug"),
            pl.col("min").mean(),
            pl.col("pts").mean(),
            pl.col("reb").mean(),
            pl.col("ast").mean(),
            pl.col("br").mean(),
            pl.col("bp").mean(),
            pl.col("tap").mean(),
            pl.col("fa").mean(),
            pl.col("mm").mean(),
            pl.col("val").mean(),
        ]
    )
    .join(clubs, on="equipo")
)

data_championsleague