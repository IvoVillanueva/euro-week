import pandas as pd
import polars as pl
from datetime import datetime, timedelta, date

semana = date.today().isocalendar().week

clubs = (
    pl.read_csv(
        "https://raw.githubusercontent.com/IvoVillanueva/acb2026/refs/heads/main/logos_calendario/clubs2026.csv"
    )
    .with_columns(pl.col("equipo").str.replace("Baskonia", "Baskonia Kosner"))
    .with_columns(
        pl.when(pl.col("equipo") == "Baskonia Kosner")
        .then(pl.lit("#000000"))
        .otherwise(pl.col("color"))
        .alias("color"),
        pl.when(pl.col("equipo") == "Baskonia Kosner")
        .then(
            pl.lit(
                "https://static.acb.com/img/www/clubes2025/2526KosnerBaskoniaLogoNegativo.png"
            )
        )
        .otherwise(pl.col("logo"))
        .alias("logo"),
    )
)

data_euroleague = (
    pl.read_csv(
        "https://raw.githubusercontent.com/IvoVillanueva/BOXSCORES-EUROLEAGE-2025_26/refs/heads/main/data/euroleague_boxscore_2025_26.csv"
    )
    .with_columns(
        pl.col("fecha").str.to_datetime("%Y-%m-%d %H:%M:%S").alias("fecha"),
        pl.col("minutes").str.replace("DNP", "0:00").alias("minutes"),
    )
    .with_columns(
        # --- Normalizar nombres de equipo ---
        pl.when(pl.col("team_name") == "KOSNER BASKONIA VITORIA-GASTEIZ")
        .then(pl.lit("Baskonia Kosner"))
        .when(pl.col("team_name") == "REAL MADRID")
        .then(pl.lit("Real Madrid"))
        .when(pl.col("team_name") == "FC BARCELONA")
        .then(pl.lit("Barça"))
        .when(pl.col("team_name") == "VALENCIA BASKET")
        .then(pl.lit("Valencia Basket"))
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
    .with_columns(
        # --- nombres correctos ---
        pl.when(pl.col("player") == "Xabi Lopez-Arostegui")
        .then(pl.lit("Xabier López-Arostegui"))
        .when(pl.col("player") == "Willy Hernangomez")
        .then(pl.lit("Willy Hernangómez"))
        .when(pl.col("player") == "Walter Tavares")
        .then(pl.lit("Edy Tavares"))
        .when(pl.col("player") == "Facundo Campazzo")
        .then(pl.lit("Facu Campazzo"))
        .when(pl.col("player") == "Nicolas Laprovittola")
        .then(pl.lit("Nico Laprovittola"))
        .when(pl.col("player") == "Andres Feliz")
        .then(pl.lit("Andrés Feliz"))
        .otherwise(pl.col("player"))
        .alias("player")
    )
    .filter(
        (
            pl.col("team_name").is_in(
                ["Baskonia Kosner", "Real Madrid", "Barça", "Valencia Basket"]
            )
        )
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
)

df_partidos_euroleague = (
    data_euroleague.group_by(["player", "equipo"])
    .agg(
        [
            pl.col("partido").n_unique().alias("jug"),
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
