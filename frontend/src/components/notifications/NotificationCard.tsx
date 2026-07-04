import { Calendar, Building2, ArrowRight } from "lucide-react";
import { Link } from "react-router-dom";
import type { Notification } from "../../types/notification";

interface NotificationCardProps {
  notification: Notification;
}

export default function NotificationCard({
  notification,
}: NotificationCardProps) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
      {/* Header */}
      <div className="flex items-center justify-between">
        <span className="rounded-full bg-blue-100 px-3 py-1 text-xs font-semibold text-blue-700">
          {notification.category || "General"}
        </span>

        <span
          className={`rounded-full px-3 py-1 text-xs font-semibold ${
            notification.status === "OPEN"
              ? "bg-green-100 text-green-700"
              : "bg-red-100 text-red-700"
          }`}
        >
          {notification.status}
        </span>
      </div>

      {/* Title */}
      <h2 className="mt-4 text-xl font-bold text-slate-900">
        {notification.exam_name}
      </h2>

      {/* Organization */}
      <div className="mt-3 flex items-center gap-2 text-slate-600">
        <Building2 size={18} />
        <span>{notification.organization}</span>
      </div>

      {/* Last Date */}
      <div className="mt-2 flex items-center gap-2 text-slate-600">
        <Calendar size={18} />
        <span>
          Apply Before :{" "}
          {notification.application_end || "Not Available"}
        </span>
      </div>

      {/* Footer */}
      <div className="mt-6 flex items-center justify-end">
        <Link
          to={`/notifications/${notification.id}`}
          className="flex items-center gap-2 font-semibold text-blue-600 transition hover:text-blue-800"
        >
          View Details
          <ArrowRight size={18} />
        </Link>
      </div>
    </div>
  );
}