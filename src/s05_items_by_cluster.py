from tm2p.enum import (
    AnalysisUnit,
    AssociationIndex,
    GraphClusteringAlgorithm,
    UnitOrderBy,
)
from tm2p.portfolio.thematic_structure.co_occurrence.direct_similarity_network import (
    ItemsByCluster,
)

df = (
    ItemsByCluster()
    #
    # UNIT OF ANALYSIS:
    .with_analysis_unit(AnalysisUnit.CONCEPT)
    #
    .having_top_n_units(100)
    .having_units_ordered_by(UnitOrderBy.OCC)
    .having_unit_occurrence_between(None, None)
    .having_unit_global_citation_between(None, None)
    .having_units_in(None)
    #
    .using_minimum_pair_co_occurrence(2)
    #
    # COUNTERS:
    .using_counters(True)
    #
    # NETWORK:
    .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    #
    # CLUSTERING:
    .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    #
    # DATABASE:
    .where_root_directory("./")
    .where_record_years_range(None, None)
    .where_record_global_citations_range(None, None)
    .where_records_match(None)
    #
    .run()
)

with open("report/items_by_cluster.txt", "w", encoding="utf-8") as f:
    f.write(df.head(50).to_string())
