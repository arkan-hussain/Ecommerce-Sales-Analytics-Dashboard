from __future__ import annotations

from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st


DATA_PATH = Path(__file__).parent / "data" / "cleaned" / "sales_orders.csv"

CATEGORY_LABELS = {
    "WL": "Weight Loss",
    "D": "Detox",
    "K": "Keto",
    "L": "Lean Bar",
    "GW": "Glow",
    "S": "Skin / Sleep",
}

STATUS_COLORS = {
    "Delivered": "#2F7D6D",
    "Returned": "#C65B4A",
    "RTO": "#8E6BBE",
}

BAR_COLORS = {
    "category": "#3B6EA8",
    "product": "#8A6A3E",
    "state": "#2F7D6D",
    "city": "#B95773",
}


st.set_page_config(
    page_title="Ecommerce Sales Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed",
)


@st.cache_data(show_spinner=False)
def load_orders() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df = df.rename(
        columns={
            "id": "order_id",
            "name": "customer_name",
            "iscod": "is_cod",
            "Date Placed": "order_date",
            "Date Delivered": "delivered_date",
            "Date Returned": "returned_date",
            "pid": "product_id",
            "Product Name": "product_name",
            "total": "revenue",
        }
    )

    date_columns = ["order_date", "delivered_date", "returned_date"]
    for column in date_columns:
        df[column] = pd.to_datetime(df[column], errors="coerce")

    text_columns = ["state", "city", "category", "status", "product_name"]
    for column in text_columns:
        df[column] = df[column].fillna("Unknown").astype(str).str.strip()

    df["category_name"] = df["category"].map(CATEGORY_LABELS).fillna(df["category"])
    df["category_display"] = df["category_name"] + " (" + df["category"] + ")"
    df["payment_method"] = df["is_cod"].map({True: "COD", False: "Prepaid"})
    df["order_day"] = df["order_date"].dt.date
    return df


def format_currency(value: float) -> str:
    return f"Rs. {value:,.0f}"


def format_percent(value: float) -> str:
    return f"{value:.1f}%"


def card(label: str, value: str, note: str) -> str:
    return f"""
    <div class="metric-card">
        <span>{label}</span>
        <strong>{value}</strong>
        <small>{note}</small>
    </div>
    """


def empty_chart(message: str) -> None:
    st.markdown(f'<div class="empty-state">{message}</div>', unsafe_allow_html=True)


def revenue_trend_chart(df: pd.DataFrame) -> alt.Chart:
    trend = (
        df.groupby("order_day", as_index=False)
        .agg(revenue=("revenue", "sum"), orders=("order_id", "nunique"))
        .sort_values("order_day")
    )
    trend["order_day"] = pd.to_datetime(trend["order_day"])

    line = (
        alt.Chart(trend)
        .mark_line(color="#2F7D6D", strokeWidth=3)
        .encode(
            x=alt.X("order_day:T", title="Date"),
            y=alt.Y("revenue:Q", title="Revenue", axis=alt.Axis(format="~s")),
            tooltip=[
                alt.Tooltip("order_day:T", title="Date", format="%d %b %Y"),
                alt.Tooltip("revenue:Q", title="Revenue", format=",.0f"),
                alt.Tooltip("orders:Q", title="Orders"),
            ],
        )
    )
    points = (
        alt.Chart(trend)
        .mark_circle(color="#2F7D6D", size=75)
        .encode(x="order_day:T", y="revenue:Q", tooltip=line.encoding.tooltip)
    )
    return (line + points).properties(height=330)


def horizontal_bar_chart(
    df: pd.DataFrame,
    group_column: str,
    label: str,
    color: str,
    limit: int | None = None,
) -> alt.Chart:
    grouped = (
        df.groupby(group_column, as_index=False)
        .agg(revenue=("revenue", "sum"), orders=("order_id", "nunique"))
        .sort_values("revenue", ascending=False)
    )
    if limit is not None:
        grouped = grouped.head(limit)

    return (
        alt.Chart(grouped)
        .mark_bar(cornerRadiusEnd=4, color=color)
        .encode(
            y=alt.Y(
                f"{group_column}:N",
                title=label,
                sort="-x",
                axis=alt.Axis(labelLimit=190),
            ),
            x=alt.X("revenue:Q", title="Revenue", axis=alt.Axis(format="~s")),
            tooltip=[
                alt.Tooltip(f"{group_column}:N", title=label),
                alt.Tooltip("revenue:Q", title="Revenue", format=",.0f"),
                alt.Tooltip("orders:Q", title="Orders"),
            ],
        )
        .properties(height=330)
    )


def status_donut_chart(df: pd.DataFrame) -> alt.LayerChart:
    status = (
        df.groupby("status", as_index=False)
        .agg(orders=("order_id", "nunique"), revenue=("revenue", "sum"))
        .sort_values("orders", ascending=False)
    )
    status["share"] = status["orders"] / status["orders"].sum()
    status["label"] = status["status"] + " " + (status["share"] * 100).round(1).astype(str) + "%"

    colors = [STATUS_COLORS.get(item, "#6D7D8B") for item in status["status"]]

    arc = (
        alt.Chart(status)
        .mark_arc(innerRadius=70, outerRadius=118, stroke="#ffffff", strokeWidth=2)
        .encode(
            theta=alt.Theta("orders:Q"),
            color=alt.Color(
                "status:N",
                title="Status",
                scale=alt.Scale(domain=list(status["status"]), range=colors),
            ),
            tooltip=[
                alt.Tooltip("status:N", title="Status"),
                alt.Tooltip("orders:Q", title="Orders"),
                alt.Tooltip("share:Q", title="Share", format=".1%"),
                alt.Tooltip("revenue:Q", title="Revenue", format=",.0f"),
            ],
        )
    )
    text = (
        alt.Chart(status)
        .mark_text(radius=145, size=12)
        .encode(theta=alt.Theta("orders:Q"), text="label:N", color=alt.value("#30343B"))
    )
    return (arc + text).properties(height=330)


def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    min_date = df["order_date"].min().date()
    max_date = df["order_date"].max().date()

    with st.container(border=True):
        filter_cols = st.columns([1.4, 1.2, 1.2, 1.2])
        date_range = filter_cols[0].date_input(
            "Date",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
            format="DD/MM/YYYY",
        )

        states = filter_cols[1].multiselect(
            "State",
            options=sorted(df["state"].unique()),
            default=[],
            placeholder="All states",
        )
        categories = filter_cols[2].multiselect(
            "Category",
            options=sorted(df["category_display"].unique()),
            default=[],
            placeholder="All categories",
        )
        statuses = filter_cols[3].multiselect(
            "Status",
            options=sorted(df["status"].unique()),
            default=[],
            placeholder="All statuses",
        )

    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date = end_date = date_range

    filtered = df[
        (df["order_date"].dt.date >= start_date)
        & (df["order_date"].dt.date <= end_date)
    ].copy()

    if states:
        filtered = filtered[filtered["state"].isin(states)]
    if categories:
        filtered = filtered[filtered["category_display"].isin(categories)]
    if statuses:
        filtered = filtered[filtered["status"].isin(statuses)]

    return filtered


def render_kpis(df: pd.DataFrame) -> None:
    revenue = df["revenue"].sum()
    orders = df["order_id"].nunique()
    aov = revenue / orders if orders else 0
    cod_pct = df["is_cod"].mean() * 100 if len(df) else 0
    delivered_pct = df["status"].str.casefold().eq("delivered").mean() * 100 if len(df) else 0

    kpi_cols = st.columns(5)
    kpis = [
        ("Revenue", format_currency(revenue), "Filtered gross sales"),
        ("Orders", f"{orders:,}", "Unique order count"),
        ("AOV", format_currency(aov), "Revenue per order"),
        ("COD %", format_percent(cod_pct), "Cash-on-delivery mix"),
        ("Delivered %", format_percent(delivered_pct), "Orders delivered"),
    ]

    for column, (label, value, note) in zip(kpi_cols, kpis):
        column.markdown(card(label, value, note), unsafe_allow_html=True)


def render_charts(df: pd.DataFrame) -> None:
    first_row = st.columns(2)
    with first_row[0]:
        st.subheader("Revenue Trend")
        st.altair_chart(revenue_trend_chart(df), width="stretch")
    with first_row[1]:
        st.subheader("Sales by Category")
        st.altair_chart(
            horizontal_bar_chart(
                df,
                "category_display",
                "Category",
                BAR_COLORS["category"],
            ),
            width="stretch",
        )

    second_row = st.columns(2)
    with second_row[0]:
        st.subheader("Order Status")
        st.altair_chart(status_donut_chart(df), width="stretch")
    with second_row[1]:
        st.subheader("Top Products")
        st.altair_chart(
            horizontal_bar_chart(
                df,
                "product_name",
                "Product",
                BAR_COLORS["product"],
                limit=10,
            ),
            width="stretch",
        )

    third_row = st.columns(2)
    with third_row[0]:
        st.subheader("State-wise Revenue")
        st.altair_chart(
            horizontal_bar_chart(
                df,
                "state",
                "State",
                BAR_COLORS["state"],
                limit=15,
            ),
            width="stretch",
        )
    with third_row[1]:
        st.subheader("Top Cities by Revenue")
        st.altair_chart(
            horizontal_bar_chart(
                df,
                "city",
                "City",
                BAR_COLORS["city"],
                limit=15,
            ),
            width="stretch",
        )


def render_css() -> None:
    st.markdown(
        """
        <style>
            :root {
                --dashboard-bg: #F5F3EF;
                --dashboard-card: #FFFFFF;
                --dashboard-text: #24272D;
                --dashboard-muted: #68717D;
                --dashboard-border: #E1DDD4;
                --dashboard-accent: #2F7D6D;
            }

            .stApp {
                background:
                    linear-gradient(180deg, rgba(47, 125, 109, 0.08), rgba(245, 243, 239, 0) 240px),
                    var(--dashboard-bg);
                color: var(--dashboard-text);
            }

            .block-container {
                padding-top: 2rem;
                padding-bottom: 2.5rem;
                max-width: 1420px;
            }

            h1 {
                color: var(--dashboard-text);
                font-size: 2.35rem;
                letter-spacing: 0;
                margin-bottom: 0.25rem;
            }

            h3 {
                color: var(--dashboard-text);
                font-size: 1.05rem;
                margin-top: 1.35rem;
            }

            [data-testid="stCaptionContainer"] {
                color: var(--dashboard-muted);
            }

            .metric-card {
                background: var(--dashboard-card);
                border: 1px solid var(--dashboard-border);
                border-radius: 8px;
                padding: 1rem 1.05rem;
                min-height: 122px;
                box-shadow: 0 10px 26px rgba(48, 52, 59, 0.055);
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }

            .metric-card span {
                color: var(--dashboard-muted);
                font-size: 0.82rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.04em;
            }

            .metric-card strong {
                color: var(--dashboard-text);
                display: block;
                font-size: clamp(1.45rem, 2.1vw, 2.15rem);
                line-height: 1.15;
                margin: 0.4rem 0;
                word-break: keep-all;
            }

            .metric-card small {
                color: var(--dashboard-muted);
                font-size: 0.82rem;
            }

            div[data-testid="stVerticalBlock"] > div:has(> .empty-state) {
                width: 100%;
            }

            .empty-state {
                background: var(--dashboard-card);
                border: 1px solid var(--dashboard-border);
                border-radius: 8px;
                color: var(--dashboard-muted);
                padding: 2rem;
                text-align: center;
            }

            div[data-testid="stHorizontalBlock"] {
                gap: 1rem;
            }

            div[data-testid="stMetric"] {
                background: var(--dashboard-card);
            }

            @media (max-width: 860px) {
                .block-container {
                    padding-left: 1rem;
                    padding-right: 1rem;
                }

                h1 {
                    font-size: 1.8rem;
                }

                .metric-card {
                    min-height: 106px;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    render_css()
    orders = load_orders()

    st.title("Ecommerce Sales Analytics Dashboard")
    st.caption(
        "Interactive sales performance view built from the cleaned order dataset."
    )

    filtered_orders = apply_filters(orders)

    if filtered_orders.empty:
        empty_chart("No orders match the selected filters. Adjust a filter to bring data back.")
        return

    render_kpis(filtered_orders)
    render_charts(filtered_orders)

    with st.expander("Filtered order data", expanded=False):
        preview_columns = [
            "order_id",
            "order_date",
            "state",
            "city",
            "category_display",
            "status",
            "payment_method",
            "quantity",
            "product_name",
            "revenue",
        ]
        st.dataframe(
            filtered_orders[preview_columns].sort_values("order_date", ascending=False),
            width="stretch",
            hide_index=True,
        )


if __name__ == "__main__":
    main()
