import NotificationCard from "./NotificationCard";
import type { Notification } from "../../types/notification";

interface NotificationListProps {
  notifications: Notification[];
}

export default function NotificationList({
  notifications,
}: NotificationListProps) {
  if (notifications.length === 0) {
    return (
      <div className="rounded-xl bg-white p-10 text-center shadow-sm">
        <p className="text-slate-500">
          No notifications found.
        </p>
      </div>
    );
  }

  return (
    <div className="grid gap-6">
      {notifications.map((notification) => (
        <NotificationCard
          key={notification.id}
          notification={notification}
        />
      ))}
    </div>
  );
}