from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
import sqlalchemy as sa

from db import load_config, make_engine


APP_TITLE = "Dashboard de Vendas — Concessionária"


@st.cache_resource(show_spinner=False)
def get_engine():
    cfg_path = Path(__file__).with_name("config.toml")
    cfg = load_config(cfg_path)
    return make_engine(cfg)


@st.cache_data(show_spinner=False, ttl=60)
def load_dim_concessionarias() -> pd.DataFrame:
    q = """
    select
      c.id_concessionarias,
      c.concessionaria,
      ci.cidade,
      e.sigla as uf
    from concessionarias c
    left join cidades ci on ci.id_cidades = c.id_cidades
    left join estados e on e.id_estados = ci.id_estados
    order by c.concessionaria
    """
    return pd.read_sql_query(q, get_engine())


@st.cache_data(show_spinner=False, ttl=60)
def load_dim_veiculos() -> pd.DataFrame:
    q = """
    select
      id_veiculos,
      nome as modelo,
      tipo,
      valor
    from veiculos
    order by nome
    """
    return pd.read_sql_query(q, get_engine())


@st.cache_data(show_spinner=False, ttl=60)
def load_sales_date_bounds() -> tuple[date | None, date | None]:
    q = "select min(data_venda) as min_data, max(data_venda) as max_data from vendas"
    df = pd.read_sql_query(q, get_engine(), parse_dates=["min_data", "max_data"])
    if df.empty:
        return None, None
    mn = df.loc[0, "min_data"]
    mx = df.loc[0, "max_data"]
    return (mn.date() if pd.notna(mn) else None, mx.date() if pd.notna(mx) else None)


@st.cache_data(show_spinner=False, ttl=60)
def load_sales_filtered(
    start: date | None,
    end: date | None,
    concessionaria_ids: list[int] | None,
    tipos: list[str] | None,
    modelos: list[str] | None,
) -> pd.DataFrame:
    where = ["1=1"]
    params: dict[str, object] = {}
    bind_params: list[sa.BindParameter] = []

    if start:
        where.append("v.data_venda >= :start")
        params["start"] = start
    if end:
        # Evita SQL com "interval" e facilita binding
        where.append("v.data_venda < :end_exclusive")
        params["end_exclusive"] = end + timedelta(days=1)

    if concessionaria_ids:
        where.append("v.id_concessionarias in :concessionaria_ids")
        params["concessionaria_ids"] = concessionaria_ids
        bind_params.append(sa.bindparam("concessionaria_ids", expanding=True))

    if tipos:
        where.append("ve.tipo in :tipos")
        params["tipos"] = tipos
        bind_params.append(sa.bindparam("tipos", expanding=True))

    if modelos:
        where.append("ve.nome in :modelos")
        params["modelos"] = modelos
        bind_params.append(sa.bindparam("modelos", expanding=True))

    q = f"""
    select
      v.id_vendas,
      v.data_venda,
      v.valor_pago,
      v.id_concessionarias,
      c.concessionaria,
      ci.cidade,
      e.sigla as uf,
      v.id_vendedores,
      vd.nome as vendedor,
      v.id_clientes,
      cl.cliente,
      v.id_veiculos,
      ve.nome as modelo,
      ve.tipo,
      ve.valor as preco_tabela
    from vendas v
    join veiculos ve on ve.id_veiculos = v.id_veiculos
    left join concessionarias c on c.id_concessionarias = v.id_concessionarias
    left join cidades ci on ci.id_cidades = c.id_cidades
    left join estados e on e.id_estados = ci.id_estados
    left join vendedores vd on vd.id_vendedores = v.id_vendedores
    left join clientes cl on cl.id_clientes = v.id_clientes
    where {" and ".join(where)}
    """

    stmt = sa.text(q)
    if bind_params:
        stmt = stmt.bindparams(*bind_params)

    df = pd.read_sql_query(stmt, get_engine(), params=params, parse_dates=["data_venda"])
    if not df.empty:
        df["mes"] = df["data_venda"].dt.to_period("M").dt.to_timestamp()
    return df


def format_brl(v: float) -> str:
    # Formatação simples e portátil (evita dependência de locale)
    s = f"{v:,.2f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"


def main():
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    st.title(APP_TITLE)

    with st.sidebar:
        st.subheader("Filtros")

        min_d, max_d = load_sales_date_bounds()
        use_date = st.checkbox("Filtrar por período", value=True)
        if use_date and min_d and max_d:
            start, end = st.date_input(
                "Período",
                value=(min_d, max_d),
                min_value=min_d,
                max_value=max_d,
            )
        else:
            start, end = None, None

        df_conc = load_dim_concessionarias()
        conc_map = dict(zip(df_conc["concessionaria"], df_conc["id_concessionarias"]))
        conc_names = st.multiselect(
            "Concessionárias (filiais)",
            options=list(conc_map.keys()),
            default=[],
        )
        conc_ids = [int(conc_map[n]) for n in conc_names] if conc_names else None

        df_vei = load_dim_veiculos()
        tipos_all = sorted([t for t in df_vei["tipo"].dropna().unique().tolist()])
        tipos = st.multiselect("Tipo de veículo", options=tipos_all, default=[])
        tipos = tipos or None

        modelos_all = sorted([m for m in df_vei["modelo"].dropna().unique().tolist()])
        modelos = st.multiselect("Modelo", options=modelos_all, default=[])
        modelos = modelos or None

        st.divider()
        st.caption("Dica: deixe filtros vazios para ver o total.")

    df = load_sales_filtered(start, end, conc_ids, tipos, modelos)

    if df.empty:
        st.info("Nenhuma venda encontrada com os filtros atuais.")
        return

    total_vendas = int(df["id_vendas"].nunique())
    receita = float(df["valor_pago"].fillna(0).sum())
    ticket_medio = receita / total_vendas if total_vendas else 0.0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total de veículos vendidos", f"{total_vendas:,}".replace(",", "."))
    c2.metric("Receita (valor pago)", format_brl(receita))
    c3.metric("Ticket médio", format_brl(ticket_medio))
    c4.metric("Modelos distintos vendidos", f"{df['modelo'].nunique():,}".replace(",", "."))

    st.divider()

    left, right = st.columns((2, 1))

    with left:
        st.subheader("Vendas por mês")
        by_month = (
            df.groupby("mes", as_index=False)
            .agg(qtd=("id_vendas", "nunique"), receita=("valor_pago", "sum"))
            .sort_values("mes")
        )
        fig = px.bar(
            by_month,
            x="mes",
            y="qtd",
            labels={"mes": "Mês", "qtd": "Veículos vendidos"},
            hover_data={"receita": ":.2f"},
        )
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("Top modelos (quantidade)")
        top_modelos = (
            df.groupby("modelo", as_index=False)
            .agg(qtd=("id_vendas", "nunique"), receita=("valor_pago", "sum"))
            .sort_values(["qtd", "receita"], ascending=False)
            .head(10)
        )
        fig = px.bar(
            top_modelos.sort_values("qtd"),
            x="qtd",
            y="modelo",
            orientation="h",
            labels={"qtd": "Vendas", "modelo": "Modelo"},
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Comparação entre filiais (concessionárias)")
    by_branch = (
        df.groupby(["concessionaria", "cidade", "uf"], as_index=False)
        .agg(qtd=("id_vendas", "nunique"), receita=("valor_pago", "sum"))
        .sort_values(["qtd", "receita"], ascending=False)
    )
    by_branch["filial"] = by_branch["concessionaria"].fillna("—") + " — " + by_branch["cidade"].fillna("—") + "/" + by_branch["uf"].fillna("—")
    fig = px.bar(
        by_branch.head(20).sort_values("qtd"),
        x="qtd",
        y="filial",
        orientation="h",
        labels={"qtd": "Veículos vendidos", "filial": "Filial"},
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Distribuição por tipo")
    by_type = (
        df.groupby("tipo", as_index=False)
        .agg(qtd=("id_vendas", "nunique"), receita=("valor_pago", "sum"))
        .sort_values("qtd", ascending=False)
    )
    fig = px.pie(by_type, names="tipo", values="qtd", hole=0.45)
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("Dados detalhados (após filtros)"):
        show_cols = [
            "data_venda",
            "concessionaria",
            "cidade",
            "uf",
            "modelo",
            "tipo",
            "valor_pago",
            "vendedor",
            "cliente",
        ]
        st.dataframe(df[show_cols].sort_values("data_venda", ascending=False), use_container_width=True)


if __name__ == "__main__":
    main()

