from tm2p.enum import AnalysisUnit  # type: ignore
from tm2p.enum import AssociationIndex  # type: ignore
from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
from tm2p.enum import NodeSizeMetric, Scaling, UnitOrderBy  # type: ignore
from tm2p.portfolio.emergence.emergence import Metrics
from tm2p.portfolio.thematic_structure.co_occurrence.direct_similarity_network import (
    NetworkPlot,
)

df = (
    Metrics()
    #
    # ANALYSIS UNIT:
    .with_analysis_unit(AnalysisUnit.CONCEPT)
    #
    # EMERGENCE:
    .using_emergence_baseline_periods(3)
    .using_emergence_recent_periods(3)
    .using_emergence_novelty_threshold(0.15)
    .using_emergence_min_total_records(7)
    .using_emergence_min_active_periods(3)
    .using_emergence_ratio_threshold(0.5)
    #
    # COUNTERS:
    .using_counters(False)
    #
    # DATABASE:
    .where_root_directory("./")
    .where_record_years_range(2016, 2025)
    .where_record_global_citations_range(None, None)
    .where_records_match(None)
    #
    .run()
)

with open("report/emergence_metrics.txt", "w", encoding="utf-8") as f:
    f.write(df.head(200).to_string())

fig = (
    NetworkPlot()
    #
    # ANALYSIS UNIT:
    .with_analysis_unit(AnalysisUnit.CONCEPT)
    #
    .having_top_n_units(None)
    .having_units_ordered_by(UnitOrderBy.OCC)
    .having_unit_occurrence_between(None, None)
    .having_unit_global_citation_between(None, None)
    .having_units_in(df.index.to_list())
    #
    .using_minimum_pair_co_occurrence(3)
    #
    # COUNTERS:
    .using_counters(False)
    #
    # NORMALIZATION:
    .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    #
    # CLUSTERING:
    .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    #
    # NETWORK:
    .using_spring_layout_k(0.15)
    .using_spring_layout_iterations(100)
    .using_spring_layout_seed(2)
    #
    .using_discrete_node_colors(
        (
            "#1f77b4",
            "#ff7f0e",
            "#2ca02c",
            "#d62728",
            "#9467bd",
            "#8c564b",
            "#e377c2",
            "#7f7f7f",
            "#bcbd22",
            "#17becf",
        )
    )
    .using_uniform_node_opacity(0.75)
    .using_node_size_metric(NodeSizeMetric.TLS)
    .using_node_scaling(Scaling.SQRT)
    .using_node_size_range(10, 80)
    .using_top_n_nodes(100)
    .using_min_node_degree(3)
    #
    .using_max_node_labels(40)
    .using_node_label_max_length(20)
    #
    .using_textfont_opacity_range(0.40, 1.00)
    .using_textfont_size_range(10, 24)
    #
    # https://www.w3schools.com/colors/colors_shades.asp
    .using_uniform_edge_color("#d8d8d8")
    .using_edge_opacity_range(0.50, 0.80)
    .using_edge_scaling(Scaling.SQRT)
    .using_global_top_edges(104)
    .using_edge_width_range(0.8, 6.0)
    .using_top_edges_per_node(5)
    #
    .using_xaxes_range(None, None)
    .using_yaxes_range(None, None)
    .using_axes_visible(False)
    #
    # DATABASE:
    .where_root_directory("./")
    .where_record_years_range(2016, 2025)
    .where_record_global_citations_range(None, None)
    .where_records_match(None)
    #
    .run()
)
fig.write_html("report/emergence_network_plot_wos.html")
