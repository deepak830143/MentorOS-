import { ReactNode } from "react";

interface StatCardProps {
  title: string;
  value: string | number;
  subtitle?: string;
  icon: ReactNode;
  color?: string;
}

function StatCard({
  title,
  value,
  subtitle,
  icon,
  color = "bg-blue-600",
}: StatCardProps) {
  return (
    <div
      className="
        bg-white
        rounded-2xl
        border
        border-slate-200
        shadow-sm
        hover:shadow-lg
        transition-all
        duration-300
        p-6
      "
    >
      <div className="flex items-start justify-between">

        <div>

          <p className="text-sm font-medium text-slate-500">
            {title}
          </p>

          <h2 className="mt-3 text-4xl font-bold text-slate-800">
            {value}
          </h2>

          {subtitle && (
            <p className="mt-2 text-sm text-slate-500">
              {subtitle}
            </p>
          )}

        </div>

        <div
          className={`
            ${color}
            p-4
            rounded-2xl
            text-white
            shadow-lg
          `}
        >
          {icon}
        </div>

      </div>
    </div>
  );
}

export default StatCard;