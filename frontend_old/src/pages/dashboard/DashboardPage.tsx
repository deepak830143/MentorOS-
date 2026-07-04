import MainLayout from "../../components/layout/MainLayout";
import StatCard from "../../components/ui/StatCard";
import { useDashboard } from "../../hooks/useDashboard";

import {
  Bell,
  Bookmark,
  Building2,
  FileText,
} from "lucide-react";

function DashboardPage() {
  const { data, isLoading, isError } = useDashboard();

  if (isLoading) {
    return (
      <MainLayout>
        <div className="flex h-[70vh] items-center justify-center">
          <h2 className="text-2xl font-semibold text-slate-600">
            Loading Dashboard...
          </h2>
        </div>
      </MainLayout>
    );
  }

  if (isError || !data) {
    return (
      <MainLayout>
        <div className="flex h-[70vh] items-center justify-center">
          <h2 className="text-2xl font-semibold text-red-600">
            Failed to load dashboard.
          </h2>
        </div>
      </MainLayout>
    );
  }

  return (
    <MainLayout>
      <div className="space-y-8">

        {/* Welcome */}

        <div>
          <h1 className="text-4xl font-bold text-slate-800">
            Welcome Back 👋
          </h1>

          <p className="mt-2 text-slate-500">
            Here's an overview of MentorOS.
          </p>
        </div>

        {/* Statistics */}

        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-4">

          <StatCard
            title="Total Notifications"
            value={data.total_notifications}
            subtitle="Collected"
            icon={<FileText size={28} />}
          />

          <StatCard
            title="Open Jobs"
            value={data.open_notifications}
            subtitle="Currently Active"
            icon={<Bell size={28} />}
            color="bg-green-600"
          />

          <StatCard
            title="Bookmarks"
            value={0}
            subtitle="Saved Jobs"
            icon={<Bookmark size={28} />}
            color="bg-pink-600"
          />

          <StatCard
            title="Organizations"
            value={data.organizations}
            subtitle="Organizations"
            icon={<Building2 size={28} />}
            color="bg-indigo-600"
          />

        </div>

        {/* Latest Notifications */}

        <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

          <h2 className="mb-6 text-2xl font-bold text-slate-800">
            Latest Notifications
          </h2>

          <div className="space-y-4">

            {data.latest_notifications.map((notification) => (

              <div
                key={notification.id}
                className="rounded-xl border border-slate-200 p-5 hover:shadow-md transition"
              >

                <h3 className="text-lg font-semibold">
                  {notification.exam_name}
                </h3>

                <p className="mt-2 text-slate-500">
                  {notification.organization}
                </p>

                <div className="mt-4 flex flex-wrap gap-3">

                  <span className="rounded-full bg-green-100 px-3 py-1 text-sm text-green-700">
                    {notification.notification_no}
                  </span>

                  <span className="rounded-full bg-blue-100 px-3 py-1 text-sm text-blue-700">
                    Apply Before: {notification.application_end}
                  </span>

                </div>

              </div>

            ))}

          </div>

        </div>

      </div>
    </MainLayout>
  );
}

export default DashboardPage;