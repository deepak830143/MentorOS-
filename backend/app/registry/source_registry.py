from app.collectors.appsc.collector import APPSCCollector


class SourceRegistry:
    """
    Registry of all notification collectors.
    """

    @staticmethod
    def get_sources():
        return {
            "appsc": APPSCCollector(),
            # "ssc": SSCCollector(),
            # "rrb": RRBCollector(),
            # "upsc": UPSCCollector(),
            # "defence": DefenceCollector(),
        }