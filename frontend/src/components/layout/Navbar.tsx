import { Bell, Search } from "lucide-react";

export default function Navbar() {
  return (
    <header className="sticky top-0 z-40 border-b border-slate-200 bg-white">
      <div className="flex h-20 items-center justify-between px-8">
        <div>
          <h1 className="text-2xl font-bold text-slate-800">
            Dashboard
          </h1>

          <p className="text-slate-500">
            Welcome back 👋
          </p>
        </div>

        <div className="flex items-center gap-6">
          <div className="relative">
            <Search
              size={18}
              className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"
            />

            <input
              type="text"
              placeholder="Search notifications..."
              className="w-80 rounded-xl border border-slate-300 py-3 pl-11 pr-4 outline-none focus:border-blue-600"
            />
          </div>

          <button className="rounded-xl border border-slate-200 p-3 hover:bg-slate-100">
            <Bell size={20} />
          </button>

          <div className="flex items-center gap-3">
            <div className="flex h-11 w-11 items-center justify-center rounded-full bg-blue-600 font-bold text-white">
              D
            </div>

            <div>
              <p className="font-semibold">
                Deepak
              </p>

              <p className="text-sm text-slate-500">
                Student
              </p>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}