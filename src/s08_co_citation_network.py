from tm2p.enum import (
    AnalysisUnit,
    AssociationIndex,
    GraphClusteringAlgorithm,
    NodeSizeMetric,
    Scaling,
)
from tm2p.portfolio.intellectual_structure.co_citation_network import NetworkPlot

plot = (
    NetworkPlot()
    #
    # ANALYSIS UNIT:
    .with_analysis_unit(AnalysisUnit.CITED_REF)
    #
    .having_top_n_cited_units(70)
    .having_minimum_cited_unit_occurrences(3)
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
    .using_spring_layout_k(0.94)
    .using_spring_layout_iterations(100)
    .using_spring_layout_seed(4)
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
    .using_node_size_metric(NodeSizeMetric.OCC)
    .using_node_scaling(Scaling.SQRT)
    .using_node_size_range(12, 80)
    .using_top_n_nodes(50)
    .using_min_node_degree(2)
    #
    .using_max_node_labels(20)
    .using_node_label_max_length(30)
    #
    .using_textfont_opacity_range(0.25, 1.00)
    .using_textfont_size_range(8, 20)
    #
    # https://www.w3schools.com/colors/colors_shades.asp
    .using_uniform_edge_color("#d8d8d8")
    .using_edge_opacity_range(0.25, 0.65)
    .using_edge_scaling(Scaling.SQRT)
    .using_global_top_edges(100)
    .using_edge_width_range(1.5, 5.0)
    .using_top_edges_per_node(5)
    #
    .using_xaxes_range(None, None)
    .using_yaxes_range(None, None)
    .using_axes_visible(False)
    #
    # DATABASE:
    .where_root_directory("./")
    .where_record_years_range(None, None)
    .where_record_global_citations_range(None, None)
    .where_records_match(None)
    #
    .run()
)
plot.write_html("report/co_citation_network_cited_ref.html")
