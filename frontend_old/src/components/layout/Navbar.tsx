import { Bell, Search, UserCircle } from "lucide-react";

function Navbar() {
  return (
    <header className="h-20 bg-white border-b border-slate-200 px-8 flex items-center justify-between">

      {/* Left */}

      <div>

        <h1 className="text-2xl font-bold text-slate-800">
          Dashboard
        </h1>

        <p className="text-sm text-slate-500">
          Welcome back to MentorOS 👋
        </p>

      </div>

      {/* Right */}

      <div className="flex items-center gap-6">

        {/* Search */}

        <div className="relative">

          <Search
            size={18}
            className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"
          />

          <input
            type="text"
            placeholder="Search notifications..."
            className="
              w-72
              rounded-xl
              border
              border-slate-200
              bg-slate-50
              py-3
              pl-11
              pr-4
              outline-none
              focus:border-blue-500
              transition
            "
          />

        </div>

        {/* Notification */}

        <button
          className="
            relative
            rounded-xl
            bg-slate-100
            p-3
            hover:bg-slate-200
            transition
          "
        >

          <Bell size={22} />

          <span
            className="
              absolute
              right-2
              top-2
              h-2.5
              w-2.5
              rounded-full
              bg-red-500
            "
          />

        </button>

        {/* User */}

        <div
          className="
            flex
            items-center
            gap-3
            rounded-xl
            bg-slate-100
            px-4
            py-2
          "
        >

          <UserCircle
            size={40}
            className="text-blue-600"
          />

          <div>

            <h2 className="font-semibold text-slate-800">
              Deepak
            </h2>

            <p className="text-sm text-slate-500">
              Student
            </p>

          </div>

        </div>

      </div>

    </header>
  );
}

export default Navbar;