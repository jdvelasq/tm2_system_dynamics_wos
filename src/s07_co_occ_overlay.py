from tm2p.enum import (
    AnalysisUnit,
    AssociationIndex,
    GraphClusteringAlgorithm,
    NodeSizeMetric,
    Scaling,
    UnitOrderBy,
)
from tm2p.portfolio.thematic_structure.co_occurrence.direct_similarity_network import (
    OverlayPlot,
)  # type: ignore

fig = (
    OverlayPlot()
    #
    # ANALYSIS UNIT:
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
    .using_counters(False)
    #
    # NORMALIZATION:
    .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    #
    # CLUSTERING:
    .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    #
    # PLOT:
    .using_spring_layout_k(0.27)
    .using_spring_layout_iterations(100)
    .using_spring_layout_seed(1)
    #
    .using_colorscale(
        [
            [0.00, "#2C7BB6"],
            [0.35, "#00A6CA"],
            [0.65, "#4EBA6F"],
            [1.00, "#F28E2B"],
        ]
    )
    .using_uniform_node_opacity(0.75)
    .using_node_size_metric(NodeSizeMetric.TLS)
    .using_node_scaling(Scaling.SQRT)
    .using_node_size_range(10, 80)
    .using_top_n_nodes(100)
    .using_min_node_degree(2)
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
    .using_global_top_edges(105)
    .using_edge_width_range(0.8, 6.0)
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
fig.write_html("report/co_occur_overlay_plot_wos.html")
