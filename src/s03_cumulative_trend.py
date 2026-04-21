from tm2p.portfolio.performance_metrics.annual_metrics import (  # type: ignore
    Column,
    RankingPlot,
)

fig = (
    RankingPlot()
    #
    .with_ranking_plotting_column(Column.CUMUL_OCC)
    #
    .using_title_text("WoS")
    .using_xaxes_title_text("Years")
    .using_yaxes_title_text("Cumulative Number of Documents")
    #
    .using_line_width(1.5)
    .using_marker_size(7)
    .using_uniform_textfont_size(10)
    .using_yshift(4)
    #
    .where_root_directory("./")
    .where_record_years_range(None, 2025)
    .where_record_global_citations_range(None, None)
    .where_records_match(None)
    #
    .run()
)
fig.write_html("report/cumulative_trend_wos.html")
