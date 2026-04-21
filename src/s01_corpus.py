from tm2p.portfolio.performance_metrics.main_metrics import Metrics  # type: ignore

df = (
    Metrics()
    #
    # DATABASE:
    .where_root_directory("./")
    .where_record_years_range(None, None)
    .where_record_global_citations_range(None, None)
    .where_records_match(None)
    #
    .run()
)

text = df.to_string()
with open("report/main_metrics.txt", "w", encoding="utf-8") as f:
    f.write(text)
