from app.collectors.appsc.collector import APPSCCollector

collector = APPSCCollector()

html = collector.collect()

print("=" * 80)
print(html)
print("=" * 80)