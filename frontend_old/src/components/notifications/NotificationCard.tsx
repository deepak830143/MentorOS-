import type { Notification } from "../../types/notification";
import {
  Building2,
  Calendar,
  Users,
  ExternalLink,
} from "lucide-react";

interface NotificationCardProps {
  notification: Notification;
}

export default function NotificationCard({
  notification,
}: NotificationCardProps) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">

      <div className="flex items-start justify-between">

        <div>

          <h2 className="text-xl font-bold text-slate-800">
            {notification.exam_name}
          </h2>

          <div className="mt-2 flex items-center gap-2 text-slate-500">
            <Building2 size={16} />
            <span>{notification.organization}</span>
          </div>

        </div>

        <span className="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-700">
          {notification.status}
        </span>

      </div>

      <div className="mt-6 grid grid-cols-2 gap-4">

        <div className="flex items-center gap-2 text-slate-600">
          <Users size={16} />
          <span>
            Vacancies: {notification.vacancies ?? "N/A"}
          </span>
        </div>

        <div className="flex items-center gap-2 text-slate-600">
          <Calendar size={16} />
          <span>
            Last Date: {notification.application_end ?? "N/A"}
          </span>
        </div>

      </div>

      <p className="mt-6 text-slate-600">
        {notification.ai_summary}
      </p>

      <div className="mt-6 flex gap-3">

        <button className="rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 transition">
          View Details
        </button>

        {notification.pdf_url && (
          <a
            href={notification.pdf_url}
            target="_blank"
            rel="noreferrer"
            className="flex items-center gap-2 rounded-lg border border-slate-300 px-4 py-2 hover:bg-slate-100 transition"
          >
            <ExternalLink size={16} />
            PDF
          </a>
        )}

      </div>

    </div>
  );
}