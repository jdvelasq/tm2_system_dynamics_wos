from tm2p.portfolio.temporal_evolution.life_cycle import LifeCyclePlot  # type: ignore

fig = (
    LifeCyclePlot()
    #
    .using_title_text("WoS")
    #
    # DATABASE:
    .where_root_directory("./")
    .where_record_years_range(None, 2025)
    .where_record_global_citations_range(None, None)
    .where_records_match(None)
    #
    .run()
)

fig.write_html("report/life_cycle_plot_wos.html")
