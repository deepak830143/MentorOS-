import {
  Bell,
  Bookmark,
  Building2,
  FileText,
} from "lucide-react";

import StatCard from "../../components/dashboard/StatCard";
import NotificationList from "../../components/notifications/NotificationList";

import { useNotifications } from "../../hooks/useNotifications";

export default function DashboardPage() {
  const { data, isLoading, error } = useNotifications();

  if (isLoading) {
    return <h2 className="text-xl">Loading...</h2>;
  }

  if (error) {
    return <h2 className="text-red-500">Failed to load notifications.</h2>;
  }

  const notifications = data ?? [];

  return (
    <div className="space-y-8">
      {/* Hero */}
      <div>
        <h1 className="text-4xl font-bold text-slate-900">
          Welcome back, Deepak 👋
        </h1>

        <p className="mt-2 text-slate-500">
          Here's an overview of MentorOS.
        </p>
      </div>

      {/* Statistics */}
      <div className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-4">
        <StatCard
          title="Notifications"
          value={notifications.length}
          icon={<FileText size={26} />}
        />

        <StatCard
          title="Open Jobs"
          value={
            notifications.filter((n) => n.status === "OPEN").length
          }
          icon={<Bell size={26} />}
          color="bg-green-600"
        />

        <StatCard
          title="Bookmarks"
          value={0}
          icon={<Bookmark size={26} />}
          color="bg-pink-600"
        />

        <StatCard
          title="Organizations"
          value={
            new Set(notifications.map((n) => n.organization)).size
          }
          icon={<Building2 size={26} />}
          color="bg-indigo-600"
        />
      </div>

      {/* Latest Notifications */}
      <div>
        <div className="mb-6 flex items-center justify-between">
          <h2 className="text-2xl font-bold">
            Latest Notifications
          </h2>

          <button className="rounded-xl border border-slate-300 px-4 py-2 hover:bg-slate-100">
            View All →
          </button>
        </div>

        <NotificationList
          notifications={notifications.slice(0, 5)}
        />
      </div>
    </div>
  );
}