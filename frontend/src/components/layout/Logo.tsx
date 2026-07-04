import { GraduationCap } from "lucide-react";

export default function Logo() {
  return (
    <div className="flex items-center gap-3">
      <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-blue-600 to-indigo-600 text-white shadow-lg">
        <GraduationCap size={24} />
      </div>

      <div>
        <h1 className="text-xl font-bold tracking-tight text-slate-900">
          MentorOS
        </h1>

        <p className="text-xs text-slate-500">
          Career Intelligence Platform
        </p>
      </div>
    </div>
  );
}