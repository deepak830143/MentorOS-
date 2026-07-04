import { useNotifications } from "../../hooks/useNotifications";
import NotificationList from "../../components/notifications/NotificationList";

export default function NotificationsPage() {
  const { data, isLoading, error } = useNotifications();

  if (isLoading) {
    return (
      <div className="p-8 text-xl">
        Loading notifications...
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-8 text-red-600">
        Failed to load notifications.
      </div>
    );
  }

  const notifications = data ?? [];

  return (
    <div className="space-y-8">

      {/* Header */}
      <div>
        <h1 className="text-4xl font-bold text-slate-900">
          Notifications
        </h1>

        <p className="mt-2 text-slate-500">
          Browse the latest government job notifications.
        </p>
      </div>

      {/* Stats */}
      <div className="rounded-2xl bg-white p-6 shadow-sm border border-slate-200">
        <p className="text-lg">
          Total Notifications
        </p>

        <h2 className="mt-2 text-4xl font-bold text-blue-600">
          {notifications.length}
        </h2>
      </div>

      {/* Notification List */}
      <NotificationList
        notifications={notifications}
      />

    </div>
  );
}