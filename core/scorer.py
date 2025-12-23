def score_paths(paths):
    for p in paths:
        p["score"] = (
            p["reliability"] * 2
            - p["noise"]
            - p["time"] * 4
        )

    return sorted(paths, key=lambda x: x["score"], reverse=True)
