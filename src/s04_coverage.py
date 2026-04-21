from tm2p.enum import Field  # type: ignore
from tm2p.ingest.records import Coverage  # type: ignore

df = (
    Coverage()
    .with_source_field(Field.CONCEPT_NORM)
    .where_root_directory("./")
    .where_record_years_range(None, 2025)
    .where_record_global_citations_range(None, None)
    .where_records_match(None)
    .run()
)

with open("report/coverage.txt", "w", encoding="utf-8") as f:
    f.write(df.to_string(index=False))
