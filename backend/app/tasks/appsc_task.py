from datetime import datetime

from app.registry.source_registry import SourceRegistry


def run_notification_engine():

    print("=" * 70)
    print("🚀 MentorOS Notification Engine Started")
    print("Time :", datetime.now())

    sources = SourceRegistry.get_sources()

    for name, collector in sources.items():

        print(f"\nChecking source : {name.upper()}")

        try:
            collector.collect()
            print(f"✅ {name.upper()} completed")

        except Exception as e:
            print(f"❌ {name.upper()} failed")
            print(e)

    print("\n🎉 Notification Engine Finished")
    print("=" * 70)