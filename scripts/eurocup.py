import pandas as pd
import polars as pl
from datetime import datetime, timedelta, date

semana = date.today().isocalendar().week

clubs = (
    pl.read_csv(
        "https://raw.githubusercontent.com/IvoVillanueva/acb2026/refs/heads/main/logos_calendario/clubs2026.csv"
    )
)

data_eurocup = (
    pl.read_csv(
        "https://raw.githubusercontent.com/IvoVillanueva/BOXSCORES-EUROLEAGE-2025_26/refs/heads/main/data/eurocup_boxscore_2025_26.csv"
    )
    .with_columns(
        pl.col("fecha").str.to_datetime("%Y-%m-%d %H:%M:%S").alias("fecha"),
        pl.col("minutes").str.replace("DNP", "0:00").alias("minutes"),
    )
    .with_columns(
        pl.when(pl.col("team_name") == "BAXI MANRESA")
        .then(pl.lit("BAXI Manresa"))
        .otherwise(pl.col("team_name"))
        .alias("team_name"),
        # --- firstName ---
        pl.when(pl.col("player").str.contains(","))
        .then(pl.col("player").str.split(", ").list.get(1).str.to_titlecase())
        .otherwise(pl.col("player").str.to_titlecase())
        .alias("firstName"),
        # --- lastName ---
        pl.when(pl.col("player").str.contains(","))
        .then(pl.col("player").str.split(", ").list.get(0).str.to_titlecase())
        .otherwise(pl.lit(None))
        .alias("lastName"),
        # --- nombre completo ---
        pl.when(pl.col("player").str.contains(","))
        .then(
            pl.col("player").str.split(", ").list.get(1).str.to_titlecase()
            + pl.lit(" ")
            + pl.col("player").str.split(", ").list.get(0).str.to_titlecase()
        )
        .otherwise(pl.col("player").str.to_titlecase())
        .alias("player"),
        # --- minutos redondeados ---
        (
            pl.col("minutes").str.split(":").list.get(0).cast(pl.Int64)
            + pl.when(pl.col("minutes").str.split(":").list.get(1).cast(pl.Int64) >= 30)
            .then(1)
            .otherwise(0)
        ).alias("minutes"),
    )
    .filter(
        (pl.col("team_name").is_in(["BAXI Manresa"]))
        & (pl.col("ronda") == pl.col("ronda").max())
        & (pl.col("semana") == semana)
    )
    .select(
        [
            "competicion",
            "fecha",
            "semana",
            "ronda",
            pl.col("id_match").alias("partido"),
            "firstName",
            "lastName",
            "player",
            pl.col("team_name").alias("equipo"),
            pl.col("minutes").alias("min"),
            pl.col("points").alias("pts"),
            pl.col("total_rebounds").alias("reb"),
            pl.col("assistances").alias("ast"),
            pl.col("steals").alias("br"),
            pl.col("turnovers").alias("bp"),
            pl.col("blocks_favour").alias("tap"),
            pl.col("fouls_commited").alias("fa"),
            pl.col("valuation").alias("val"),
            pl.col("plusminus").alias("mm"),
        ]
    )
    .sort("player")
    .join(clubs, on="equipo")
)

df_partidos_eurocup = (
    data_eurocup.group_by(["player", "equipo"])
    .agg(
        [
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
    .sort("player")
    .join(clubs, on="equipo")
)
