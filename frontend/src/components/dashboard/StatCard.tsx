import type { ReactNode } from "react";

interface StatCardProps {
  title: string;
  value: number;
  icon: ReactNode;
  color?: string;
}

export default function StatCard({
  title,
  value,
  icon,
  color = "bg-blue-600",
}: StatCardProps) {
  return (
    <div className="group rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">
      <div className="flex items-start justify-between">
        <div>
          <p className="text-sm font-medium text-slate-500">
            {title}
          </p>

          <h2 className="mt-4 text-5xl font-bold text-slate-900">
            {value}
          </h2>
        </div>

        <div
          className={`${color} flex h-14 w-14 items-center justify-center rounded-2xl text-white`}
        >
          {icon}
        </div>
      </div>
    </div>
  );
}