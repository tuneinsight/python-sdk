from enum import Enum


class VisualizationType(str, Enum):
    COUNT = "count"
    HISTOGRAM = "histogram"
    SURVIVALCURVE = "survivalCurve"
    TABLE = "table"
    INTERSECTIONTABLE = "intersectionTable"
    MANHATTANPLOT = "manhattanPlot"
    LINE = "line"
    STATISTICS = "statistics"

    def __str__(self) -> str:
        return str(self.value)
